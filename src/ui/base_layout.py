import streamlit as st


def style_base_layout():
    st.markdown(
        """
        <style>
        /* 1. Import Montserrat, Outfit, Fredoka & Luckiest Guy Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Luckiest+Guy&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&family=Outfit:wght@100..900&display=swap');

        /* 2. FORCE THE DYNAMIC MOVING MESH BACKGROUND UNIVERSALLY */
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

        /* Target the internal container card inside modals/dialog pops to clear white space */
        [data-testid="stDialog"] [data-testid="stMarkdownContainer"], 
        div[role="dialog"] > div {
            background-color: transparent !important;
            color: #FFFFFF !important;
        }

        /* 3. Clean up default Streamlit headers and footers */
        #MainMenu, footer, header, [data-testid="stHeader"] {
            visibility: hidden !important;
            height: 0px !important;
        }
                
        .block-container {
            padding-top: 2rem !important;    
        }

        /* 4. Headings & Text Styling */
        h1, h1 span, h1 div {
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            font-size: 3.5rem !important;
            color: #FFFFFF !important;
            line-height: 1.1 !important;
        }
                
        h2, h2 span, h2 div {
            font-family: 'Fredoka', sans-serif !important;
            font-weight: 700 !important;
            font-size: 2rem !important;
            color: #FFFFFF !important;
            line-height: 1.2 !important;
        }
                
        h3, h4, p, h3 span, h4 span, p span, li {
            font-family: 'Fredoka', sans-serif !important; 
            color: #FFFFFF !important;
        }

        /* Input Labels */
        label p {
            color: #FFFFFF !important;
            font-family: 'Outfit', sans-serif !important;
        }
                
        /* Make sure Form Text inputs blend natively over your dark teal background */
        .stTextInput position, div[data-baseweb="input"] {
            background-color: rgba(255, 255, 255, 0.15) !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
            border-radius: 8px !important;
        }
        
        div[data-baseweb="input"] input {
            color: #FFFFFF !important;
            font-family: 'Outfit', sans-serif !important;
        }
                
        /* --- 5. GLOBAL POP ART "BUTTON-53" OVERRIDES --- */
        div.stButton > button, 
        div.stDownloadButton > button,
        div.stDownloadButton > a,
        button, 
        [data-testid="stBaseButton-secondary"] {
            background-color: #3DD1E7 !important;
            border: 3px solid #000000 !important; /* Thick comic casing */
            box-sizing: border-box !important;
            color: #000000 !important;
            display: flex !important;
            
            /* FORCE PUNCHY COMIC TYPOGRAPHY */
            font-family: 'Luckiest Guy', cursive !important;
            font-size: 1.15rem !important;       /* Keeps text elements on a single row */
            letter-spacing: 0.5px !important;
            text-transform: uppercase !important; 
            
            justify-content: center !important;
            align-items: center !important;      /* Centers inner elements perfectly */
            line-height: 1.2rem !important;       
            padding: .6rem 1rem !important;       
            position: relative !important;
            text-align: center !important;
            text-decoration: none !important;
            width: 100% !important;
            max-width: 460px !important;
            cursor: pointer !important;
            transform: rotate(-2deg) !important; /* Organic comic book tilt angle */
            user-select: none !important;
            -webkit-user-select: none !important;
            touch-action: manipulation !important;
            border-radius: 12px !important; 
            box-shadow: 4px 4px 0px #000000 !important; /* Flat heavy retro drop shadow */
            transition: all 0.1s ease !important;
            white-space: nowrap !important;      /* Critical single-row locking parameter */
        }

        /* Strip child typography tag margins to prevent alignment bugs */
        div.stButton > button p, 
        div.stDownloadButton > button p,
        div.stDownloadButton > a span,
        button p {
            font-family: 'Luckiest Guy', cursive !important;
            color: #000000 !important;
            font-size: 1.15rem !important;
            white-space: nowrap !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        div.stButton > button:focus,
        div.stDownloadButton > button:focus,
        div.stDownloadButton > a:focus,
        button:focus {
            outline: 0 !important;
            box-shadow: 2px 2px 0px #000000 !important;
            color: #000000 !important;
        }

        div.stButton > button:hover,
        div.stDownloadButton > button:hover,
        div.stDownloadButton > a:hover,
        button:hover,
        [data-testid="stBaseButton-secondary"]:hover {
            background-color: #A3FFF4 !important; /* Glow up neon highlight on interaction hover */
            color: #000000 !important;
            transform: rotate(-2deg) scale(1.02) !important;
            box-shadow: 6px 6px 0px #000000 !important;
        }
        
        div.stButton > button:active,
        div.stDownloadButton > button:active,
        div.stDownloadButton > a:active,
        button:active {
            transform: scale(0.98) rotate(-2deg) !important;
            box-shadow: 2px 2px 0px #000000 !important;
        }

        /* Desktop Media Breakpoint: Scale text sizes and padding cleanly for wide windows */
        @media (min-width: 768px) {
            div.stButton > button,
            div.stDownloadButton > button,
            div.stDownloadButton > a,
            button {
                padding: .75rem 2rem !important;  
                font-size: 1.35rem !important;    
            }
            div.stButton > button p, 
            div.stDownloadButton > button p,
            button p {
                font-size: 1.35rem !important;
            }
        }

        /* --- 6. PATCH: ISOLATE AND REVERT DIALOG POPUP BUTTONS TO NORMAL --- */
        [data-testid="stDialog"] button, 
        [data-testid="stDialog"] div.stButton > button,
        [data-testid="stDialog"] [data-testid="stBaseButton-secondary"] {
            background-color: transparent !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            color: #FFFFFF !important;
            font-family: 'Outfit', sans-serif !important;
            font-size: 1rem !important;
            text-transform: none !important;
            transform: none !important;
            box-shadow: none !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
            letter-spacing: normal !important;
            width: auto !important;
            display: inline-flex !important;
        }

        [data-testid="stDialog"] button p,
        [data-testid="stDialog"] div.stButton > button p {
            font-family: 'Outfit', sans-serif !important;
            color: #FFFFFF !important;
            font-size: 1rem !important;
            text-transform: none !important;
        }

        /* Dialog Button Hover State */
        [data-testid="stDialog"] button:hover, 
        [data-testid="stDialog"] div.stButton > button:hover {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-color: #FFFFFF !important;
            color: #FFFFFF !important;
            transform: none !important;
            box-shadow: none !important;
        }
        </style>  
        """,
        unsafe_allow_html=True,
    )