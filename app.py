from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title = "Vineet Puranik's Portfolio", page_icon=":memo:",layout = "wide")
##page_icon is an emoji & layout sets the page to wide view

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


##Load Assets
lottie_coding = "https://lottie.host/63542cfc-a0ee-42d5-b7a0-fcbef38db824/uFbSpST8XH.json"
img_org_form = Image.open("images/findmyorg.png")
img_website = Image.open("mywebsite.png")
##header section
with st.container():
    st.subheader("Hi, I'm Vineet :wave:")
    image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXH8T6ExrVJYZz3DhiCDw_ErfvwLwkwRAAlw&s'  
    col1, col2 = st.columns([1, 1]) 
    with col1:
        st.title("Current junior studying MIS at UT Austin!")
    with col2:
        st.image(image_url, width=100)  
    st.write("Welcome to my website! Dive into my journey of blending modern technology and design. This summer, I'm on a mission to create and launch a standout product.")
    st.markdown(
        '<a href="https://www.linkedin.com/in/vineet-puranik/" style="color:black; text-decoration: none; border-bottom: 1px solid black;">Go ahead, check out my LinkedIn! It\'s like peeking into my diary, but without the embarrassing moments 🙂</a>',
        unsafe_allow_html=True
    )

#What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("A little about me!")
        st.write("#####")
        st.write(
            """
            As a student at the University of Texas at Austin, I am engaged in a variety of extracurriculars, leadership and volunteering oppurtunities, and projects
            - FindMyOrg.com
            - The Texas Rocket Engineering Laboratory
            - The Undergraduate Business Council
            - Project Advance Austin
            - The Austin Public Library
            """
        )
        st.markdown(
        '<a href="https://docs.google.com/document/d/1p1GkDCL2HJWm_qMQkU41XXNCc3-vpcQBPbZ6HF2QckQ/edit?usp=sharing" style="color:black; text-decoration: none; border-bottom: 1px solid black;">Check out my Resume ></a>',
        unsafe_allow_html=True
        )
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")
## --- Projects ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_org_form)
    with text_column:
        st.subheader("FindMyOrg.com")
        st.write(
            """
             Just got to campus? Are you overwhelmed by the shear amount of organizations on campus?
             FindMyOrg is a web application that consolidates campus organizations in order to help you find your home on the 40 acres.
             Check out the website, and receive a curated list of organizations based on our demands.
             Explore the organizations of your dreams right from your room!
            """
        )
        st.markdown("[Explore FindMyOrg!](https://findmyorg.com/)")
    with st.container():
        image_column, text_column = st.columns((1,2))
    with image_column:
        with image_column:
            st.image(img_website)
        with text_column:
            st.subheader("Vineet Puranik's Portfolio")
            st.write(
                """
                Want to create your website! Trial and Error. 
                Perfection take time.
                Follow this source code to develop a website for your  business, blog, portfolio, or any other purpose!
                """
            )
            st.markdown("[Take a look the code...]()")









