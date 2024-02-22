import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

# title
st.title("Optical Character Recognition for  Dyslexia")

# subtitle
st.markdown("## Using `easyocr`, `streamlit`")

st.markdown("")

# image uploader
image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])


@st.cache
def load_model():
    reader = ocr.Reader(['en'], model_storage_directory='.')
    return reader


reader = load_model()  # load model

if image is not None:
    input_image = Image.open(image)  # read image
    st.image(input_image)  # display image

    with st.spinner("Loading"):
        result = reader.readtext(np.array(input_image))

        result_text = []  # empty list for results
        for text in result:
            result_text.append(text[1])

        # Specify the font for the result text
        result_text_html = "<div style='font-family: OpenDyslexic;'>"
        for text in result_text:
            result_text_html += text + "<br>"
        result_text_html += "</div>"

        # Display the result text with the specified font
        st.markdown(result_text_html, unsafe_allow_html=True)

else:
    st.write("Upload an Image")
