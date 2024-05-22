import base64
import streamlit as st
import random
import requests

st.title("ARE YOU IN DESPERATE NEED OF CAT MEMES?")

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
        [data-testid="stHorizontalBlock"]::first-of-type {{
            background-color: red;
        }}
    .block-container{{
        background: rgba(255, 255, 255, .6)
    }}
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

st.markdown(f"""<p>Welcome to the ultimate destination for all cat lovers! 😻</p>
<p>Here you will find the most hilarious, adorable, and relatable cat memes that will brighten up your day. Whether you need a break from work, a mood booster, or just some furry fun, we have got you covered.</p>
<p>To get started, just click on the button below and enjoy a random cat meme from our collection. Have fun and meow! 🐾</p>
""", unsafe_allow_html=True)


def get_drive_images(folder_url, api_key):
    folder_id = folder_url.split('/')[-1]
    
    response = requests.get(f'https://www.googleapis.com/drive/v3/files?q=\'{folder_id}\' in parents and trashed=false&key={api_key}')
    
    if response.status_code == 200:
        files = response.json().get('files', [])
        image_files = [file for file in files if file['mimeType'].startswith('image/')]
        return image_files
    else:
        st.warning("Error fetching files from Google Drive. Please check the folder URL.")
        return []


def display_random_image(images):
    if not images:
        st.warning("No image files found in the Google Drive folder.")
        return

    random_image = random.choice(images)
    image_id = random_image.get('id', '')

    if not image_id:
        st.warning("Could not find a valid image ID.")
        return

    image_url = f'https://drive.google.com/thumbnail?id={image_id}&sz=w1000'
    # temporary solution as Google API does experience issues now
    # see more: https://stackoverflow.com/questions/77803187/having-trouble-displaying-an-image-from-google-drive

    try:
        st.image(image_url, caption="Random cat meme from our collection, enjoy <3")
    except Exception as e:
        st.warning(f"Error loading the image: {str(e)}")
        st.text("Placeholder: Image Not Available")


google_drive_folder_url = "https://drive.google.com/drive/folders/1Yxz_BH7nzdxwo_YixPJZ_QH4XzyQLy9x"
google_api_key = "AIzaSyAaowfbullxQUxn6-gayoK8uq_c2fMl5NU"

image_files = get_drive_images(google_drive_folder_url, google_api_key)

if st.button("Show me a cat meme"):
    display_random_image(image_files)
    

