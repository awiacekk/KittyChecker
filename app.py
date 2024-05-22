import base64
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from keras.models import load_model
import cv2
from keras.applications.densenet import preprocess_input
import tensorflow as tf
from st_pages import Page, show_pages

def predict(image, path):
    left_co, cent_co,last_co = st.columns(3)
    with left_co:
        waiting = st.image('waiting.gif')
        img = cv2.resize(image, (224,224), interpolation = cv2.INTER_AREA)
        dim = np.expand_dims(img, axis=0).astype(np.float32)
        dim = preprocess_input(dim)
        model = load_model(path)
        pred = model.predict(dim, verbose = 0)
        preds = np.array(tf.nn.softmax(pred))
        waiting.empty()
    return preds

st.set_page_config(page_title="KittyChecker", page_icon = 'logo.png')

st.markdown(
        f"""
        <style>
            [data-testid="stSidebar"] {{
                background: linear-gradient(#F8F8FF, #FFFACD);
                position: relative;
                display: flex;
            }}
            [data-testid="stSidebarNav"]::before {{
                content: "KittyChecker";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 36px;
                position: relative;
                top: 50px;
                font-weight: bold;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

show_pages(
    [
        Page("app.py", "Main page", ":star:"),
        Page("pages/adoption.py", "About adoption", ":house:"),
        Page("pages/breeds.py", "Cat breeds", ":cat2:"),
        Page("pages/memes.py", "Cat memes", ":joy_cat:"),
    ]
)


st.markdown(
    f"""
     <style>
     .stApp {{
        background: url(data:image/{'jpg'};base64,{base64.b64encode(open('background.jpg', "rb").read()).decode()});
        background-repeat: no-repeat;
        width: auto;
        height: 100%;
        background-size: cover;
        background-attachment: fixed;
     }}
     </style>
     """,
    unsafe_allow_html=True,
)

st.title('Load your cat photo')
df = pd.read_csv('indexes.csv')

def main():
    uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg', 'jpeg'])
    options = ['DenseNet121', 'InceptionV3', 'ResNet101']
    option = st.selectbox(
            "Choose your model",
            options,
            index=0
            )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        image = cv2.cvtColor(img_array, cv2.IMREAD_COLOR)
        if image is not None:
            if option == options[0]:
                model_path = 'models/densenet121.h5'
            elif option == options[1]:
                model_path = 'models/inceptionV3.h5'
            else:
                model_path = 'models/resnet101.h5'

            preds = predict(image, model_path)
            st.markdown(f"<p style='background-color:#ffffff;opacity: 0.5;font-size:16px;text-align: center;'>{df['Breed'][0]} {f'{preds[0][0]:.2%}'}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='background-color:#ffffff;opacity: 0.5;font-size:16px;text-align: center;'>{df['Breed'][1].replace('_', ' ')} {f'{preds[0][1]:.2%}'}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='background-color:#ffffff;opacity: 0.5;font-size:16px;text-align: center;'>{df['Breed'][2].replace('_', ' ')} {f'{preds[0][2]:.2%}'}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='background-color:#ffffff;opacity: 0.5;font-size:16px;text-align: center;'>{df['Breed'][3]} {f'{preds[0][3]:.2%}'}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='background-color:#ffffff;opacity: 0.5;font-size:16px;text-align: center;'>{df['Breed'][4]} {f'{preds[0][4]:.2%}'}</p>", unsafe_allow_html=True)
            st.image(image, use_column_width=True)


if __name__ == '__main__':
    main()

