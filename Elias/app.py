import streamlit as st
from PIL import Image

import os
import pandas as pd


from io import BytesIO
CARPETA_CARGA = 'uploads'

st.set_page_config(page_title="letsGoThesis", page_icon="📚", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>SISTEMA WEB INTELIGENTE PARA LA DETECCIÓN DE AGENTES PLAGA EN LA PRODUCCIÓN DE TOMATE 🍅</h1>", 
    unsafe_allow_html=True
)

def resize_image(image, size=(300, 200)):
    return image.resize(size)


with st.container():
    #st.header("Hi 👋 somos💻 letsGoThesis  👨‍🎓")
    if __name__ == "__main__":
        opcion = st.sidebar.radio("Seleccionar Procesamiento", ["Imagen", "Video"])
        archivo_cargado = st.file_uploader(f"", type=["jpg", "jpeg", "png"])

       # Obtener la ruta absoluta del archivo de imagen
        current_dir = os.path.dirname(__file__)
        imagen_path = os.path.join(current_dir, "imagenes", "fondoTesis.png")

        # Mostrar la imagen en Streamlit
        Image_fondo = st.columns(1)[0]
        with Image_fondo:
            image = Image.open(imagen_path)
            st.image(image, use_column_width=True)

# Configuración de la cadena de conexión
def get_connection_string():
    secrets = st.secrets["connections"]["mysql"]
    return f"mysql+mysqlconnector://{secrets['username']}:{secrets['password']}@{secrets['host']}:{secrets['port']}/{secrets['database']}?charset={secrets['query']['charset']}"

# Realizar consulta y obtener datos
def fetch_data(engine):
    query = "SELECT * FROM plagas"
    df = pd.read_sql(query, engine)
    return df
  
# Main
def main():
    st.title("Aplicación de Tesis")
    st.write("Mostrando datos de la tabla 'plagas'.")

    connection_string = get_connection_string()
    engine = create_engine(connection_string)
    
    df = fetch_data(engine)
    if not df.empty:
        for row in df.itertuples():
            st.write(f"{row.name}")
    else:
        st.write("No se encontraron datos en la tabla 'plagas'.")

if __name__ == "__main__":
    main()

with st.container():
        
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h2 style='text-align: start;'>Escríbemos 📝</h2>", unsafe_allow_html=True)
        st.write("Dejámos tu mensaje y enseguida te respondemos")
        image = Image.open("imagenes/dev.png") 
        image = resize_image(image)
        st.image(image, use_column_width=True)
    
    with col2:
        st.write("Este es un formulario de contácto, no de preguntas y respuestas. Cualquier duda sobre el desarrollo y funcionamiento del sistema.")
        with st.form(key='contact_form'):
            name = st.text_input("Nombre")
            email = st.text_input("Email")
            message = st.text_area("Mensaje")
            
            
             # Estilo CSS para el botón
            st.markdown(
                """
                <style>
                .stButton>button {
                    width: 100%;
                    background-color: #007BFF;
                    color: white;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            submit_button = st.form_submit_button(label='Enviar 🔐')
            
            if submit_button:
                if not name:
                    st.error("Por favor, ingrese su nombre.")
                elif not email:
                    st.error("Por favor, ingrese su email.")
                elif not message:
                    st.error("Por favor, ingrese su mensaje.")
                else:
                    st.success("Gracias por contactarnos, nos pondremos en contacto contigo pronto.")

