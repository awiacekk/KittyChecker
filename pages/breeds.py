import base64
import streamlit as st


st.title("Cat breeds")

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

st.markdown(f"""
<p>By adopting a cat from a shelter or rescue you are:</p>
<ul><li>saving a life.</li>
<li>helping with pet overpopulation.</li>
<li>saving money because the cost of adopting is much less than buying from a breeder or pet store.</li>
<li>getting a knowledgeable opinion from pet rescue staff on the best fit for you since all cats are assessed for the type of home they would fit best.</li></ul>
<p style="line-height:1.5">When thinking about adopting a cat, it is important to research what characteristics each breed is known for.  All cats are different, so it is important to spend time with any cat you are thinking about adopting to make sure you are the purr-fect friends for each other.  Here are some breeds and their characteristics that we most often see at Gilbertsville Veterinary Hospital.</p>
<h3>Siamese</h3><p style="line-height:1.5">They require attention. Siamese cats are 100 percent committed to building a relationship with you and will go out of their way to make sure you know you are their best friend. They are very vocal cats, opinionated and will let you know if you are ignoring then. When adopting a Siamese be prepared to commit the love and attention they need.</p>
<h3>Maine Coon</h3><p style="line-height:1.5">Main Coon cats are very social animals, enjoy the company of the family but are not needy. They are known to greet their humans and come when called and tend to be goofy.  They are playful, very intelligent and tend to not be lap cats but do like to be near you.</p>
<h3>Domestic Shorthair Cat<h3><p style="line-height:1.5">The Domestic shorthair comes in a wide array of colors, sizes, and statures, though they tend to be medium-sized and muscular. They have short, sleek coats and round heads and paws. Because of their mixed parentage, Domestic Shorthairs don't tend to be at-risk for any unusual health complications.</p>
<h3>Bengal<h3><p style="line-height:1.5">The Bengal is a sleek, muscular cat with a wild appearance, enhanced by the bold marbling and spotting on their thick, luxurious coat. Despite their striking appearance, physically there is nothing extreme about their build or structure, as this is a well-balanced cat without any exaggerated features, smallish ears, wedge shaped head, neat paws and athletic outline. Bengals make fabulous pets for experienced cat owners who love an active, curious and dog-like cat - and can keep them entertained with toys, games and plenty of environmental enrichment.</p>
<h3>Ragdoll</h3><p style="line-height:1.5">Ragdoll cats have a relaxed and friendly personality, which make them ideal family pets. They enjoy being with humans and often seek out attention and strokes. Ragdolls are very wonderful companions as they are empathetic and in tune with human emotions. They are loyal and playful, despite being one of the largest domestic breeds of cats; bred to have extremely soft coats and attractive blue eyes.</p>
""", unsafe_allow_html=True)
