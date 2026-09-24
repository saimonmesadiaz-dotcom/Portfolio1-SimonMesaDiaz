import streamlit as st
from PIL import Image
st.title("Portafolio 1 - Creación de Interfaces multimodales")
st.subheader('Creado por: Simón Mesa Díaz')
image = Image.open('SimonImagen.png')
st.image(image, width=650)

with st.sidebar:
  st.subheader("Aplicaciones e Interfaces Multimodales y de Inteligencia Artificial creadas con GitHub y Streamlit.")
  parrafo = (
    "Este portafolio reúne las actividades desarrolladas durante la primer mitad del curso de Creación de Interfaces"
    " Multimodales, donde estamos explorando diferentes herramientas y tecnologías de inteligencia artificial"
    " aplicadas a la interacción digital. A través de ejercicios de procesamiento de texto, audio e imágenes, "
    " reconocimiento de voz, visión artificial y aprendizaje automático, experimenté con distintas formas de crear "
    " interfaces más interactivas, accesibles y dinámicas."
  )
  st.write(parrafo)
  
col1, col2, col3 = st.columns(3)
with col1:
 
 st.subheader("Mi primer repositorio - Introducción a GitHub")
 image = Image.open('SnoopyP.jpg')
 st.image(image, width=190)
 st.write("Exploración inicial de GitHub como herramienta para el desarrollo y publicación de interfaces. Se realizó el primer repositorio y se experimentó con modificaciones visuales y transformaciones básicas de imágenes dentro de una interfaz web.") 
 url = "https://el-primer-repo-de-saimon-fnendgpad7jxzqwkawtxsa.streamlit.app/"
 st.write(f"Repositorio Snoopy: [Enlace]({url})")

 st.subheader("Texto a voz - Conversión de fragmentos de texto en audio")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("Desarrollo de una interfaz para convertir texto escrito en audio, explorando herramientas de síntesis de voz. La actividad permitió comprender cómo estas tecnologías facilitan la interacción con contenidos escritos y sirven como base para interfaces multimodales y asistentes de voz.") 
 url = "https://gaticorat-cxqqen2bqdsebk6fnnoapf.streamlit.app/"
 st.write(f"Texto a Voz: [Enlace]({url})")

 st.subheader("Voz a texto multilingüe — Reconocimiento de voz")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("Creación de una interfaz capaz de transformar audio de voz en texto en diferentes idiomas, incluyendo español, inglés, francés, italiano, alemán y mandarín. La actividad permitió experimentar con el reconocimiento automático del lenguaje y sus posibilidades de interacción.") 
 url = "https://traductorsimon-cwqeceiewyudz2ktpf6hzh.streamlit.app/"
 st.write(f"Traductor: [Enlace]({url})")

 st.subheader("Imagen a texto - Reconocimiento Óptico de Caracteres (OCR)")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("Implementación de OCR para extraer texto a partir de imágenes. La actividad permitió explorar cómo una imagen con información escrita puede ser procesada y convertida en texto editable, aplicando conceptos de visión artificial y procesamiento de información.") 
 url = "https://ocr-audiosimon-abfnnjajxn75g8upksqeq6.streamlit.app/"
 st.write(f"Reconocimietno óptico caracteres: [Enlace]({url})")

with col2: 
 st.subheader("Interfaz final — OCR y análisis estadístico - Temática playera")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("Desarrollo de una interfaz multimodal de conversión de imagen a texto, complementada con un análisis estadístico de las vocales identificadas en el contenido extraído. La propuesta incorporó una temática playera para integrar el procesamiento de texto con una experiencia visual más personalizada.") 
 url = "https://ocr-audiosimon-awv2toavjnd8nxdt7uuqvh.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("WordCloud: Nube de palabras — Procesamiento de lenguaje natural")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("Creación de nubes de palabras (WordCloud) a partir de fragmentos de texto para representar visualmente los términos más relevantes. Se exploró el uso de TextBlob y técnicas de procesamiento de lenguaje natural para analizar y transformar información textual en recursos gráficos.") 
 url = "https://wordcloudsimon-5ftjecuahge5koe5fvwyka.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Análisis de sentimientos - Emociones e interacción")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("Desarrollo de una interfaz para identificar sentimientos y emociones presentes en un texto. Los resultados se complementaron con recursos visuales y audiovisuales, como animaciones de Lottie y videos asociados a las emociones detectadas, creando una experiencia multimodal.") 
 url = "https://sentimentasimon-kxq5k5hfxwdmkofrfih48x.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Evaluación automática — TF-IDF y extracción de información")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("Creación de una interfaz para generar preguntas y respuestas automáticas a partir de textos mediante técnicas de procesamiento de lenguaje natural. Se utilizó TF-IDF para identificar términos relevantes dentro de un conjunto de documentos y facilitar la extracción de información para la generación de respuestas.") 
 url = "https://tdfespsimon-735v6pnj9zjcvmgf2qrjwv.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("YOLO — Reconocimiento y detección de objetos")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("Exploración del modelo YOLO (You Only Look Once) para el reconocimiento y detección de objetos en imágenes. La actividad permitió comprender cómo la inteligencia artificial puede interpretar información visual y localizar diferentes elementos dentro de una escena.") 
 url = "https://t8pwvf7om2y4dwtcjzvsyu.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")
 
 st.subheader("Teachable Machine — Reconocimiento de gestos y objetos")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("Experimentación con Teachable Machine de Google para entrenar modelos personalizados de aprendizaje automático. Se realizaron pruebas de reconocimiento de personas, objetos y gestos, comprendiendo de manera práctica cómo los modelos pueden aprender patrones a partir de ejemplos y utilizarlos en tiempo real.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


