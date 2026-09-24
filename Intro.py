st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

/* =====================================================
   FONDO GENERAL
===================================================== */

.stApp {
    background: linear-gradient(
        135deg,
        #061826 0%,
        #083B4C 35%,
        #087F8C 70%,
        #20C9C3 100%
    );
    color: white;
    font-family: 'Poppins', sans-serif;
}


/* =====================================================
   CONTENEDOR PRINCIPAL
===================================================== */

.block-container {
    max-width: 1550px;
    padding-top: 3rem;
    padding-left: 3rem;
    padding-right: 3rem;
    padding-bottom: 4rem;
}


/* =====================================================
   TÍTULO PRINCIPAL
===================================================== */

h1 {
    text-align: center !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 42px !important;
    font-weight: 800 !important;
    color: white !important;
}


/* =====================================================
   SUBTÍTULOS
===================================================== */

h2, h3 {
    text-align: center !important;
    font-family: 'Poppins', sans-serif !important;
    color: white !important;
    font-weight: 700 !important;
}


/* =====================================================
   TEXTO NORMAL
===================================================== */

p {
    font-family: 'Poppins', sans-serif !important;
    font-size: 14px !important;
    line-height: 1.65 !important;
    color: #E8FFFF !important;
    text-align: center !important;
}


/* =====================================================
   COLUMNAS
===================================================== */

[data-testid="column"] {
    background: rgba(255, 255, 255, 0.10);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 20px;
    padding: 25px;
    margin: 8px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}


/* =====================================================
   TÍTULOS DE LAS ACTIVIDADES
===================================================== */

[data-testid="column"] h3 {
    text-align: center !important;
    font-size: 18px !important;
    line-height: 1.35 !important;
    min-height: 50px;
}


/* =====================================================
   CENTRAR IMÁGENES
===================================================== */

[data-testid="stImage"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
}

[data-testid="stImage"] img {
    display: block;
    margin-left: auto !important;
    margin-right: auto !important;
    border-radius: 15px;
    box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.30);
}


/* =====================================================
   ENLACES
===================================================== */

a {
    color: #8FFFF8 !important;
    font-weight: 600 !important;
    text-decoration: none !important;
}

a:hover {
    color: white !important;
    text-decoration: underline !important;
}


/* =====================================================
   SIDEBAR COLOR CREMA
===================================================== */

section[data-testid="stSidebar"] {
    background: #F3E8D0 !important;
}


/* =====================================================
   TEXTO DEL SIDEBAR
===================================================== */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #171717 !important;
    text-align: center !important;
    font-weight: 700 !important;
}

section[data-testid="stSidebar"] p {
    color: #171717 !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
    text-align: center !important;
}


/* =====================================================
   ELEMENTOS INTERNOS DEL SIDEBAR
===================================================== */

section[data-testid="stSidebar"] * {
    color: #171717;
}


/* =====================================================
   LÍNEA DECORATIVA
===================================================== */

hr {
    border: none;
    height: 2px;
    background: linear-gradient(
        90deg,
        transparent,
        #5FFFF5,
        transparent
    );
    margin: 30px 0;
}


/* =====================================================
   OCULTAR ELEMENTOS DE STREAMLIT
===================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)
