from langchain_core.documents import Document
import streamlit as st
from langchain_community.document_loaders.text import TextLoader
import os
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
import uuid

def load_all_pdfs():
    folder_path = "src/database"
    num_docs = 0
    all_docs = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            # complete file path
            pdf_path = os.path.join(folder_path, filename)

            loader = PyPDFLoader(pdf_path)
            doc = loader.load()
            
            all_docs.extend(doc)
            num_docs += 1

    print("total pdfs:", num_docs)
    print("total pages:", len(all_docs))
    return all_docs


def split_docs(documents, chunk_size=75, chunk_overlap=20):
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )

    chunked_docs = text_splitter.split_documents(documents)
    return chunked_docs

class EmbeddingManager:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        
        self.model_name=model_name
        print("loading model....", self.model_name)
        self.model = SentenceTransformer(self.model_name)
        print("embedding dimensions=", self.model.get_sentence_embedding_dimension())


    def generate_embeddings(self, text):
        embeddings = self.model.encode(text, show_progress_bar=True)
        print("embeddings shape:", embeddings.shape)
        return embeddings
    
class VectorStoreManager:
    def __init__(self, persist_directory="src/database", collection_name="pdf_documents"):
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        self.collection = None
        self.client = None

        self._initialize_store()

    def _initialize_store(self):
        os.makedirs(self.persist_directory, exist_ok=True)
        
        # create a client
        self.client = chromadb.PersistentClient(path=self.persist_directory)

        # create the collection
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"description": "vector store collection for pdf embeddings in RAG"}
        )

        print("initialized the vector store with collection:", self.collection_name)
        print("docs in collection:", self.collection.count())

    def add_documents(self, documents, embeddings):
        if len(documents) != len(embeddings):
            raise ValueError("num of documents does not match num of embeddings")


        # store => ids, embedding, document, metadata
        ids = []
        all_metadata = []
        documents_content = []
        embeddings_list = []

        for i, (doc, embedding) in enumerate(zip(documents, embeddings)):
            doc_id = f"doc_{uuid.uuid4()}"
            ids.append(doc_id)

            metadata = dict(doc.metadata)
            metadata["doc_index"] = i
            metadata["content_length"] = len(doc.page_content)
            all_metadata.append(metadata)

            documents_content.append(doc.page_content)

            embeddings_list.append(embedding.tolist())

            self.collection.add(
                ids=ids,
                metadatas=all_metadata,
                documents=documents_content,
                embeddings=embeddings_list
            )

        print("total documents added in vector store=", len(documents_content))
        print("docs in collection:", self.collection.count())

class RAGRetriever:
    def __init__(self, embedding_manager, vector_store):
        self.embedding_manager = embedding_manager
        self.vector_store = vector_store


    def retrieve(self, query, top_k=5, score_threshold=0.0):
        # query => embedding
        query_embeddings = self.embedding_manager.generate_embeddings([query])[0]

        # semantic search
        results = self.vector_store.collection.query(
            query_embeddings=[query_embeddings.tolist()],
            n_results=top_k
        )

        # cosine similarity
        retrieved_docs=[]
        
        if results["documents"] and results["documents"][0]:
            ids = results["ids"][0]
            metadatas = results["metadatas"][0]
            documents = results["documents"][0]
            distances = results["distances"][0]

            for i, (doc_id, metadata, document, distance) in enumerate(zip(ids, metadatas, documents, distances)):
                similarity_score = 1 - distance

                if similarity_score >= score_threshold:
                    retrieved_docs.append({
                        "id": doc_id,
                        "document": document,
                        "metadata": metadata,
                        "distance": distance,
                        "similarity_score": similarity_score,
                        "rank" : i + 1
                    })

            print(f"retrieved {len(retrieved_docs)} documents")

        else:
            print("no documents found")

        return retrieved_docs

from groq import Groq

def generate_output(query, retriever, client, top_k=3):

    results = retriever.retrieve(
        query=query,
        top_k=top_k
    )

    context = "\n\n".join(
        [doc["document"] for doc in results]
    )

    if not context:
        return "I couldn't find any relevant information in the documents."

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

CONTEXT:
{context}

QUESTION:
{query}

If the answer is not present in the context,
say:
'I could not find that information in the documents.'
"""

    completion = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {
                "role": "system",
                "content": "You answer questions using provided documents only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


@st.cache_resource
def initialize_rag():

    docs = load_all_pdfs()

    chunks = split_docs(docs)

    embedding_manager = EmbeddingManager()

    vector_store = VectorStoreManager()

    if vector_store.collection.count() == 0:

        embeddings = embedding_manager.generate_embeddings(
            [chunk.page_content for chunk in chunks]
        )

        vector_store.add_documents(
            chunks,
            embeddings
        )

    retriever = RAGRetriever(
        embedding_manager,
        vector_store
    )

    return retriever