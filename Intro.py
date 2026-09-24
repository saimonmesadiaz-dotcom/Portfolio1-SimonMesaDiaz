import streamlit as st
from PIL import Image

# =========================================================
# CONFIGURACIÓN DE LA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Portafolio - Interfaces Multimodales",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# ESTILOS CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');


/* =========================================================
   FONDO GENERAL
========================================================= */

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


/* =========================================================
   CONTENEDOR PRINCIPAL
========================================================= */

.block-container {
    max-width: 1550px;
    padding-top: 3rem;
    padding-left: 4rem;
    padding-right: 4rem;
    padding-bottom: 4rem;
}


/* =========================================================
   TÍTULO PRINCIPAL
========================================================= */

h1 {
    text-align: center !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 42px !important;
    font-weight: 800 !important;
    color: white !important;
    margin-bottom: 0.3rem !important;
}


/* =========================================================
   SUBTÍTULOS
========================================================= */

h2,
h3 {
    text-align: center !important;
    font-family: 'Poppins', sans-serif !important;
    color: white !important;
    font-weight: 700 !important;
}


/* =========================================================
   TÍTULOS DE LAS ACTIVIDADES
========================================================= */

[data-testid="column"] h3 {
    text-align: center !important;
    font-size: 19px !important;
    line-height: 1.35 !important;
    min-height: 55px;
}


/* =========================================================
   TEXTO NORMAL
========================================================= */

p {
    font-family: 'Poppins', sans-serif !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
    color: #E8FFFF !important;
    text-align: center !important;
}


/* =========================================================
   IMÁGENES
========================================================= */

[data-testid="stImage"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
}

[data-testid="stImage"] img {
    display: block !important;
    margin-left: auto !important;
    margin-right: auto !important;
    border-radius: 15px !important;
    box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.30);
}


/* =========================================================
   COLUMNAS / TARJETAS
========================================================= */

[data-testid="column"] {
    background: rgba(255, 255, 255, 0.10);

    border: 1px solid rgba(255, 255, 255, 0.18);

    border-radius: 20px;

    padding: 25px;

    margin: 10px;

    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}


/* =========================================================
   ENLACES
========================================================= */

a {
    color: #8FFFF8 !important;
    font-weight: 600 !important;
    text-decoration: none !important;
}

a:hover {
    color: white !important;
    text-decoration: underline !important;
}


/* =========================================================
   SIDEBAR COLOR CREMA
========================================================= */

section[data-testid="stSidebar"] {
    background: #F3E8D0 !important;
}


/* =========================================================
   TEXTO DEL SIDEBAR
========================================================= */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {

    color: #171717 !important;

    text-align: center !important;

    font-family: 'Poppins', sans-serif !important;

    font-weight: 700 !important;
}


section[data-testid="stSidebar"] p {

    color: #171717 !important;

    font-family: 'Poppins', sans-serif !important;

    font-size: 14px !important;

    line-height: 1.7 !important;

    text-align: center !important;
}


/* Hace que cualquier otro texto del sidebar sea negro */

section[data-testid="stSidebar"] * {
    color: #171717;
}


/* =========================================================
   LÍNEA DECORATIVA
========================================================= */

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


/* =========================================================
   OCULTAR ELEMENTOS DE STREAMLIT
========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ENCABEZADO
# =========================================================

st.title("Portafolio 1")

st.subheader("Creación de Interfaces Multimodales")

st.markdown(
    """
    <p style="
        text-align:center;
        font-size:18px !important;
    ">
        Creado por: <strong>Simón Mesa Díaz</strong>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# IMAGEN PRINCIPAL
# =========================================================

image = Image.open("SimonImagen.png")

st.image(
    image,
    width=650
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.subheader(
        "Aplicaciones e Interfaces Multimodales y de Inteligencia Artificial"
    )

    parrafo = (
        "Este portafolio reúne las actividades desarrolladas durante la "
        "primera mitad del curso de Creación de Interfaces Multimodales, "
        "donde estamos explorando diferentes herramientas y tecnologías "
        "de inteligencia artificial aplicadas a la interacción digital. "
        "A través de ejercicios de procesamiento de texto, audio e imágenes, "
        "reconocimiento de voz, visión artificial y aprendizaje automático, "
        "experimenté con distintas formas de crear interfaces más interactivas, "
        "accesibles y dinámicas."
    )

    st.write(parrafo)


# =========================================================
# COLUMNAS
# =========================================================

col1, col2, col3 = st.columns(3, gap="large")


# =========================================================
# COLUMNA 1
# =========================================================

with col1:

    st.subheader("Mi primer repositorio — Introducción a GitHub")

    image = Image.open("SnoopyP.jpg")
    st.image(image, width=190)

    st.write(
        "Exploración inicial de GitHub como herramienta para el desarrollo "
        "y publicación de interfaces. Se realizó el primer repositorio y "
        "se experimentó con modificaciones visuales y transformaciones "
        "básicas de imágenes dentro de una interfaz web."
    )

    url = "https://el-primer-repo-de-saimon-fnendgpad7jxzqwkawtxsa.streamlit.app/"
    st.write(f"🔗 Repositorio Snoopy: [Enlace]({url})")


    st.subheader("Texto a voz — Conversión de texto en audio")

    image = Image.open("txt_to_audio.png")
    st.image(image, width=200)

    st.write(
        "Desarrollo de una interfaz para convertir texto escrito en audio, "
        "explorando herramientas de síntesis de voz. La actividad permitió "
        "comprender cómo estas tecnologías facilitan la interacción con "
        "contenidos escritos y sirven como base para interfaces multimodales."
    )

    url = "https://gaticorat-cxqqen2bqdsebk6fnnoapf.streamlit.app/"
    st.write(f"🔗 Texto a Voz: [Enlace]({url})")


    st.subheader("Voz a texto multilingüe — Reconocimiento de voz")

    image = Image.open("Traduccion.avif")
    st.image(image, width=200)

    st.write(
        "Creación de una interfaz capaz de transformar audio de voz en "
        "texto en diferentes idiomas, incluyendo español, inglés, francés, "
        "italiano, alemán y mandarín."
    )

    url = "https://traductorsimon-cwqeceiewyudz2ktpf6hzh.streamlit.app/"
    st.write(f"🔗 Traductor: [Enlace]({url})")


    st.subheader("Imagen a texto — Reconocimiento Óptico de Caracteres")

    image = Image.open("Playa.jpg")
    st.image(image, width=200)

    st.write(
        "Implementación de OCR para extraer texto a partir de imágenes. "
        "La actividad permitió explorar cómo una imagen con información "
        "escrita puede ser procesada y convertida en texto editable."
    )

    url = "https://ocr-audiosimon-abfnnjajxn75g8upksqeq6.streamlit.app/"
    st.write(f"🔗 Reconocimiento óptico de caracteres: [Enlace]({url})")


# =========================================================
# COLUMNA 2
# =========================================================

with col2:

    st.subheader("Interfaz final — OCR y análisis estadístico")

    image = Image.open("Playa.jpg")
    st.image(image, width=200)

    st.write(
        "Desarrollo de una interfaz multimodal de conversión de imagen "
        "a texto, complementada con un análisis estadístico de las vocales "
        "identificadas en el contenido extraído. La propuesta incorporó "
        "una temática playera para integrar el procesamiento de texto "
        "con una experiencia visual personalizada."
    )

    url = "https://ocr-audiosimon-awv2toavjnd8nxdt7uuqvh.streamlit.app/"
    st.write(f"🔗 OCR y análisis: [Enlace]({url})")


    st.subheader("WordCloud — Nube de palabras")

    image = Image.open("data_analisis.png")
    st.image(image, width=190)

    st.write(
        "Creación de nubes de palabras a partir de fragmentos de texto "
        "para representar visualmente los términos más relevantes. "
        "Se exploró el uso de TextBlob y técnicas de procesamiento "
        "de lenguaje natural."
    )

    url = "https://wordcloudsimon-5ftjecuahge5koe5fvwyka.streamlit.app/"
    st.write(f"🔗 WordCloud: [Enlace]({url})")


    st.subheader("Análisis de sentimientos — Emociones e interacción")

    image = Image.open("OIG3.jpg")
    st.image(image, width=200)

    st.write(
        "Desarrollo de una interfaz para identificar sentimientos y "
        "emociones presentes en un texto. Los resultados se complementaron "
        "con animaciones de Lottie y videos asociados a las emociones "
        "detectadas."
    )

    url = "https://sentimentasimon-kxq5k5hfxwdmkofrfih48x.streamlit.app/"
    st.write(f"🔗 Análisis de sentimientos: [Enlace]({url})")


# =========================================================
# COLUMNA 3
# =========================================================

with col3:

    st.subheader("Evaluación automática — TF-IDF")

    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)

    st.write(
        "Creación de una interfaz para generar preguntas y respuestas "
        "automáticas a partir de textos mediante técnicas de procesamiento "
        "de lenguaje natural. Se utilizó TF-IDF para identificar términos "
        "relevantes dentro de un conjunto de documentos."
    )

    url = "https://tdfespsimon-735v6pnj9zjcvmgf2qrjwv.streamlit.app/"
    st.write(f"🔗 TF-IDF: [Enlace]({url})")


    st.subheader("YOLO — Reconocimiento y detección de objetos")

    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)

    st.write(
        "Exploración del modelo YOLO (You Only Look Once) para el "
        "reconocimiento y detección de objetos en imágenes. La actividad "
        "permitió comprender cómo la inteligencia artificial puede "
        "interpretar información visual."
    )

    url = "https://t8pwvf7om2y4dwtcjzvsyu.streamlit.app/"
    st.write(f"🔗 YOLO: [Enlace]({url})")


    st.subheader("Teachable Machine — Reconocimiento de gestos y objetos")

    image = Image.open("OIG6.jpg")
    st.image(image, width=200)

    st.write(
        "Experimentación con Teachable Machine de Google para entrenar "
        "modelos personalizados de aprendizaje automático. Se realizaron "
        "pruebas de reconocimiento de personas, objetos y gestos en tiempo real."
    )

    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"🔗 Teachable Machine: [Enlace]({url})")
