import base64
import streamlit as st


st.title("About adoption")

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

st.markdown(f"""<p>If you are looking for a kitten of a specific breed, this article is for you. I will explain everything you need to know to find an ethical breeder and the red flags you should be careful about. You will see that there are many criteria and you can’t just pick up the first ad you see: you’ll need to do some research first. If this sounds complicated, I strongly recommend that you do not compromise on this: we are talking about the health of a kitten! If you don’t want to go through all the hassle, maybe look for a kitten at your local shelter: they will know what’s best for the kittens and you can be fairly sure they’ll do all the necessary checks.
<h3>The pedigree, aka a proof.</h3>
<p>First thing first, a kitten from a breeder should have a pedigree. A pedigree is a registration paper that certifies that your kitten belongs to a breed. It also contains the genealogy of the cat (generally 4 or 5 generations). For it to be reliable, a pedigree is generally issued by a reputable cat breed registry such as the TICA, Fifé, WCF, LOOF, CFA… depending on where you live. This means that the cattery is registered at one of those associations. This is something that you should be able to verify on their website.</p>
<p>The pedigree is the reflection of the work of a reputable breeder: you can verify that the breeder didn’t reproduce a mother with a son, or a brother and a sister for example.</p>
<p>With websites such as Pawpeds, you can also calculate the inbreeding coefficient of your cat. The lower the inbreeding coefficient, generally the better. It’s recommended to stay below 5% \\for 10 generations.</p>
<p>Without a pedigree, you have no proof that your cat belongs to a breed (No, there isn’t any DNA test for cat breeds as explained in this article). If you are looking for a cat without a pedigree, why not look at your local cat shelter? You will find many awesome cats and it will be another good way to responsibly adopt a cat.</p>
<p>If the breeder asks for more money to give you the pedigree or claims that you don’t need one because you won’t breed the kitten: run!</p>
<p>All “breeders” breeding cats without a pedigree are backyard breeders.</p>
<p>However, finding a breeder that sells kittens with a pedigree is not enough! Many breeders breeding cats with pedigrees are not ethical nor reputable: that’s why there are many other important criteria beyond the papers.</p>
""", unsafe_allow_html=True)
