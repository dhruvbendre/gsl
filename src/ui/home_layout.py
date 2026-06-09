import streamlit as st


def home_header():
    # 1. INJECT ANIMATED BACKGROUND & COSCO-STYLE POP ART OVERRIDES EXCLUSIVELY FOR HOME
    st.markdown(
        """
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
        }

        /* Target the internal container card inside modals/dialog pops to clear white space */
        [data-testid="stDialog"] [data-testid="stMarkdownContainer"], 
        div[role="dialog"] > div {
            background-color: transparent !important;
            color: #FFFFFF !important;
        }

        /* --- GLOBAL NATIVE STREAMLIT BUTTON OVERRIDES ("BUTTON-53" POP ART DESIGN) --- */
        /* Target BOTH normal buttons and download buttons explicitly */
        div.stButton > button, 
        div.stDownloadButton > button,
        div.stDownloadButton > a {
            background-color: #3DD1E7 !important;
            border: 3px solid #000000 !important; /* Thick comic casing */
            box-sizing: border-box !important;
            color: #000000 !important;
            display: flex !important;
            
            /* --- FORCE PUNCHY "LUCKIEST GUY" TYPOGRAPHY FOR KIDS --- */
            font-family: 'Luckiest Guy', cursive !important;
            font-size: 1.15rem !important;       /* Adjusted down to keep long labels on one row */
            letter-spacing: 0.5px !important;
            text-transform: uppercase !important; 
            
            justify-content: center !important;
            align-items: center !important;      /* Centers text vertically inside the button */
            line-height: 1.2rem !important;       /* Tightened line height prevents container clipping */
            padding: .6rem 1rem !important;       /* Clean padding gives text breathing room */
            position: relative !important;
            text-align: center !important;
            text-decoration: none !important;
            width: 100% !important;
            max-width: 460px !important;
            cursor: pointer !important;
            transform: rotate(-2deg) !important; /* Classic organic tilt angle */
            user-select: none !important;
            -webkit-user-select: none !important;
            touch-action: manipulation !important;
            border-radius: 12px !important; /* Thick curved block edges */
            box-shadow: 4px 4px 0px #000000 !important; /* Flat heavy retro shadow dropped down */
            transition: all 0.1s ease !important;
            white-space: nowrap !important;      /* CRITICAL: Disallows text wrapping entirely */
        }

        /* Prevent Streamlit inner paragraph markers from stepping on the comic typography choice */
        div.stButton > button p, 
        div.stDownloadButton > button p,
        div.stDownloadButton > a span {
            font-family: 'Luckiest Guy', cursive !important;
            color: #000000 !important;
            font-size: 1.15rem !important;
            white-space: nowrap !important;      /* Forces inner text components to never warp */
            margin: 0 !important;                /* Strip default layout spacing margins */
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
            background-color: #A3FFF4 !important; /* Glow up neon highlight on interaction hover */
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

        /* Desktop Media Breakpoint: Scales up sizing cleanly when screen allows */
        @media (min-width: 768px) {
            div.stButton > button,
            div.stDownloadButton > button,
            div.stDownloadButton > a {
                padding: .75rem 2rem !important;  /* Strategic horizontal desktop spacing */
                font-size: 1.35rem !important;    /* Clean size configuration that avoids breaks */
            }
            div.stButton > button p, 
            div.stDownloadButton > button p {
                font-size: 1.35rem !important;
            }
        }

        /* --- END OF BUTTON-53 LAYERING --- */

        /* Centered Hero Header Container */
        .hero-container {
            display: flex !important;
            justify-content: center !important; 
            align-items: center !important;     
            width: 100% !important;
            padding-top: 1rem !important;
            padding-bottom: 0rem !important; 
            margin-bottom: -1.5rem !important; 
            text-align: center !important;      
        }
        
        /* THE ANIMATED MEGA HEADER */
        .mega-header {
            font-family: 'Montserrat', sans-serif;
            font-size: 6.5rem !important;  
            font-weight: 900 !important;   
            letter-spacing: -4px !important; 
            line-height: 0.85 !important;
            margin: 0 auto !important; 
            text-transform: uppercase;
            display: inline-block;
            background: linear-gradient(to right, #FFFFFF 20%, #A3FFF4 40%, #00E5FF 60%, #FFFFFF 80%);
            background-size: 200% auto;
            -webkit-background-clip: text !important;
            background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            animation: shineShimmer 4s linear infinite !important;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }

        @keyframes shineShimmer {
            0% { background-position: 0% center; transform: scale(1); }
            50% { transform: scale(1.015); }
            100% { background-position: -200% center; transform: scale(1); }
        }
                
        .sub-header {
            font-family: 'Fredoka', sans-serif !important;
            font-weight: 600 !important;
            font-size: 2rem !important;   
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

        /* --- NEW: MOBILE RESPONSIVE MEDIA BREAKPOINTS --- */
        @media (max-width: 992px) {
            .mega-header { font-size: 4.5rem !important; letter-spacing: -2px !important; }
        }

        /* Targeted Mobile Breakpoint (Phones) */
        @media (max-width: 740px) {
            /* Kill default left-alignment on all Streamlit parent wrapper containers */
            .hero-container, 
            .hero-container div, 
            [data-testid="stMarkdownContainer"] .hero-container {
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                text-align: center !important;
                width: 100% !important;
                margin: 0 auto !important;
            }
            
            /* ADDED: Kill the layout space of the link anchor to prevent visual shifting */
            .hero-container a.element-anchor {
                display: none !important;
                width: 0px !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            
            .mega-header { 
                font-size: 2.8rem !important;     /* Fits 'HACKATHON' onto a single row cleanly */
                letter-spacing: 0px !important;   /* Eliminates horizontal spacing bias gaps */
                line-height: 1.1 !important;      
                text-align: center !important;
                margin: 0 auto !important;
                display: block !important;        /* Structural switch overrides default element constraints */
                width: 100% !important;
            }
            
            .sub-header {
                font-size: 1.4rem !important;    
                text-align: center !important;
                width: 100% !important;
            }
            
            .block-container {
                padding-top: 1rem !important;    
            }
        }
                
        /* --- INFO CARDS HORIZONTAL 3-COLUMN LAYOUT --- */
        .card-container {
            display: grid;
            grid-template-columns: 1fr; /* Defaults to single column for mobile screen boundaries */
            gap: 1.5rem;
            width: 100%;
            padding: 1rem 0rem;
        }

        /* Tablet & Desktop Breakpoint: Forces exactly 3 items inline without breaking layouts */
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

        /* Fun hover animation when kids or parents mouse over the cards */
        .info-card:hover {
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 8px 8px 0px #000000 !important;
            background-color: rgba(255, 255, 255, 0.18) !important;
            border-color: #A3FFF4 !important; /* Soft glowing border highlight */
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
            color: #A3FFF4 !important; /* Bright cyan titles look crisp against dark teal */
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
        """,
        unsafe_allow_html=True,
    )

    # 2. RENDER THE MEGA TITLE
    st.markdown(
        """
        <div class="hero-container">
            <h2 class="mega-header">HACKATHON STEM</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )