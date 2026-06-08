import streamlit as st

def home_header():
    # 1. INJECT ANIMATED BACKGROUND & COSCO-STYLE POP ART OVERRIDES EXCLUSIVELY FOR HOME
    st.markdown("""
        <style>
        /* Import the perfect playful font combo: Fredoka & Luckiest Guy */
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Luckiest+Guy&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&family=Outfit:wght@100..900&display=swap');

        /* Dynamic Moving Mesh Background forced on all root layout wrappers AND dialogues/modals */
        .stApp, .stMain, [data-testid="stAppViewContainer"], [data-testid="stDialog"] div[role="dialog"], [data-testid="stModal"] {
            background: linear-gradient(-45deg, #005f52, #009A88, #00CBB4, #004d43) !important;
            background-size: 400% 400% !important;
            animation: gradientMove 12s ease infinite !important;
            background-attachment: fixed !important;
        }

        @keyframes gradientMove {
            0% { background-position: 0% 50% !important; }
            50% { background-position: 100% 50% !important; }
            100% { background-position: 0% 50% !important; }
        }

        /* 3. Clean up default Streamlit headers and footers */
        #MainMenu, footer, header, [data-testid="stHeader"] {
            visibility: hidden !important;
            height: 0px !important;
        }
                
        .block-container {
            padding-top: 2rem !important;    
            max-width: 100% !important; /* Ensures the container utilizes full layout width */
        }

        /* Target the internal container card inside modals/dialog pops to clear white space */
        [data-testid="stDialog"] [data-testid="stMarkdownContainer"], 
        div[role="dialog"] > div {
            background-color: transparent !important;
            color: #FFFFFF !important;
        }

        /* --- GLOBAL NATIVE STREAMLIT BUTTON OVERRIDES ("BUTTON-53" POP ART DESIGN) --- */
        div.stButton > button, 
        div.stDownloadButton > button,
        div.stDownloadButton > a {
            background-color: #3DD1E7 !important;
            border: 3px solid #000000 !important;
            box-sizing: border-box !important;
            color: #000000 !important;
            display: flex !important;
            font-family: 'Luckiest Guy', cursive !important;
            font-size: 1.15rem !important;      
            letter-spacing: 0.5px !important;
            text-transform: uppercase !important; 
            justify-content: center !important;
            align-items: center !important;      
            line-height: 1.2rem !important;       
            padding: .6rem 1rem !important;       
            position: relative !important;
            text-align: center !important;
            text-decoration: none !important;
            width: 100% !important;
            max-width: 460px !important;
            cursor: pointer !important;
            transform: rotate(-2deg) !important; 
            user-select: none !important;
            -webkit-user-select: none !important;
            touch-action: manipulation !important;
            border-radius: 12px !important; 
            box-shadow: 4px 4px 0px #000000 !important; 
            transition: all 0.1s ease !important;
            white-space: nowrap !important;      
        }

        div.stButton > button p, 
        div.stDownloadButton > button p,
        div.stDownloadButton > a span {
            font-family: 'Luckiest Guy', cursive !important;
            color: #000000 !important;
            font-size: 1.15rem !important;
            white-space: nowrap !important;      
            margin: 0 !important;                
            padding: 0 !important;
        }

        div.stButton > button:focus,
        div.stDownloadButton > button:focus,
        div.stDownloadButton > a:focus {
            outline: 0 !important;
            box-shadow: 2px 2px 0px #000000 !important;
            color: #000000 !important;
        }

        div.stButton > button:hover,
        div.stDownloadButton > button:hover,
        div.stDownloadButton > a:hover {
            background-color: #A3FFF4 !important; 
            color: #000000 !important;
            transform: rotate(-2deg) scale(1.02) !important;
            box-shadow: 6px 6px 0px #000000 !important;
        }
        
        div.stButton > button:active,
        div.stDownloadButton > button:active,
        div.stDownloadButton > a:active {
            transform: scale(0.98) rotate(-2deg) !important;
            box-shadow: 2px 2px 0px #000000 !important;
        }

        @media (min-width: 768px) {
            div.stButton > button,
            div.stDownloadButton > button,
            div.stDownloadButton > a {
                padding: .75rem 2rem !important;  
                font-size: 1.35rem !important;    
            }
            div.stButton > button p, 
            div.stDownloadButton > button p {
                font-size: 1.35rem !important;
            }
        }

        /* --- HERO CONTAINER UPDATES --- */
        .hero-container {
            display: flex;
            justify-content: center; 
            align-items: center;     
            width: 100%;
            padding: 1rem 0rem !important;
            margin: 0 auto !important;
            text-align: center;      
            overflow: hidden; /* Prevents text overflow leaks */
        }
        
        /* THE FLUID MEGA HEADER */
        .mega-header {
            font-family: 'Montserrat', sans-serif;
            /* Uses fluid sizing (11% of the total viewport width) with constraints */
            font-size: clamp(2.8rem, 11vw, 6.5rem) !important;  
            font-weight: 900 !important;   
            letter-spacing: -0.05em !important; /* Relative spacing scales with font size */
            line-height: 0.9 !important;
            margin: 0 auto !important; 
            text-transform: uppercase;
            display: inline-block;
            background: linear-gradient(to right, #FFFFFF 20%, #A3FFF4 40%, #00E5FF 60%, #FFFFFF 80%);
            background-size: 200% auto;
            -webkit-background-clip: text !important;
            background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            animation: shineShimmer 4s linear infinite !important;
            white-space: nowrap !important; /* Prevents word breakdown splitting */
        }

        @keyframes shineShimmer {
            0% { background-position: 0% center; transform: scale(1); }
            50% { transform: scale(1.015); }
            100% { background-position: -200% center; transform: scale(1); }
        }
                
        .sub-header {
            font-family: 'Fredoka', sans-serif !important;
            font-weight: 600 !important;
            font-size: clamp(1.3rem, 4vw, 2rem) !important;   
            color: #FFFFFF !important;
            margin-top: 0.8rem !important; 
            margin-bottom: 0px !important;
            padding: 0 !important;
            letter-spacing: 0px !important; 
        }
        
        h3, h4, p, h3 span, h4 span, p span, li {
            font-family: 'Fredoka', sans-serif !important; 
            color: #FFFFFF !important;
        }

        /* Responsive padding safety drop for tiny screen profiles */
        @media (max-width: 576px) {
            .block-container {
                padding-top: 1rem !important;    
            }
        }
                
        /* --- INFO CARDS HORIZONTAL 3-COLUMN LAYOUT --- */
        .card-container {
            display: grid;
            grid-template-columns: 1fr; 
            gap: 1.5rem;
            width: 100%;
            padding: 1rem 0rem;
        }

        @media (min-width: 768px) {
            .card-container {
                grid-template-columns: repeat(3, 1fr) !important;
            }
        }

        .info-card {
            background-color: rgba(255, 255, 255, 0.12) !important;
            border: 3px solid #000000 !important;
            border-radius: 16px !important;
            padding: 1.5rem !important;
            box-shadow: 5px 5px 0px #000000 !important;
            transition: all 0.2s ease-in-out !important;
            color: #FFFFFF !important;
            display: flex;
            flex-direction: column;
        }

        .info-card:hover {
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 8px 8px 0px #000000 !important;
            background-color: rgba(255, 255, 255, 0.18) !important;
            border-color: #A3FFF4 !important; 
        }

        .card-icon {
            font-size: 2.2rem !important;
            margin-bottom: 0.5rem !important;
            display: inline-block;
        }

        .card-title {
            font-family: 'Fredoka', sans-serif !important;
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: #A3FFF4 !important; 
            margin: 0.2rem 0rem 0.6rem 0rem !important;
            line-height: 1.3 !important;
        }

        .card-body {
            font-family: 'Outfit', sans-serif !important;
            font-size: 1.05rem !important;
            font-weight: 400 !important;
            color: #FFFFFF !important;
            line-height: 1.5 !important;
            margin: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. RENDER THE MEGA TITLE
    st.markdown("""
        <div class="hero-container">
            <h2 class="mega-header">HACKATHON</h2>
        </div>
    """, unsafe_allow_html=True)