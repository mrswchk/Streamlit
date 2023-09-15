from datetime import datetime
import pandas as pd
from PIL import Image
import json
import requests
import streamlit as st 
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="Fall 2023", page_icon=":cherry_blossom:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---- Header Section-----

st.title("UTD Fall 2023 CLASSES :fallen_leaf:")
st.subheader(" Quick overview of the classes I have to attend for fall 2023! Good Luck!")
st.markdown(":orange[***Trying to get the classes their locations and textbooks for the classes all in one place so that it stays nice and organized.***]")


#---LOAD ADDESTS----

lottie_coding = load_lottieurl("https://lottie.host/5225386e-b49f-4fe6-8bf8-c26864bb1000/WK1oviIb7v.json")
img_contact_phy = Image.open("images/phy.png")
img_contact_math =Image.open("images/math.png")
img_contact_CS = Image.open("images/CS.png")
img_contact_film = Image.open("images/Film.png")

#--- what i do -- 
st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("What I do")
    st.write("##")
    data_df = pd.DataFrame(
        {
            "CLASSTIME":[
                datetime(2023,9,19,10,0),
                datetime(2023,9,19,13,0),
                datetime(2023,9,19,16,0),
                datetime(2023,9,20,16,00),
                datetime(2023,9,21,10,0),
                datetime(2023,9,21,13,0),
                datetime(2023,9,21,16,0),
                datetime(2023,9,22, 10,00),
                datetime(2023,9,22, 13,00),


            ]
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "CLASSTIME": st.column_config.DatetimeColumn(
                "CLASSTIME",
                min_value=datetime(2023,6,1),
                max_value=datetime(2025,1,1),
                format="MM D YYYY, h:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )

    st.markdown("**WEEKLY CLASS TIME!**")
with right_column:
    st_lottie(lottie_coding, height=500,key="coding")


# --- this is the place where I wanna do differebt columns so 
# two and then like an image subject and then  short summary on the other
# LIKE A BIG SUBJECT HEADER AN IMAGE FROM LOTTIE AND THEN ON THE SMALLER SIDE ITS THE SHORT SUMMARY. ---

with st.container():
    st.write("---")
    st.header("My classes")
    st.write("###")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_phy)
    with text_column: 
        st.header(":orange[PHYSICS] [TUE/THUR] 1PM - 2:15PM")
        st.write("PHYS 2326.002 ELECTROMAGNETISM AND WAVES A continuation of PHYS 2325, topics include electrostatics and electromagnetics, electric field and potential, electric currents, magnetic fields law of Coulomn, Ampere, Faraday and Maxwell's theory.")
        st.subheader(":globe_with_meridians: :blue[***location***] SCI 1.220")
        st.markdown(":orange[**THE TEXTBOOK:**][ TEXTBOOK LINK >](https://drive.google.com/file/d/1rkW6tNSOB4l1T2T9vk6irRS9Is1ghMwF/view?usp=sharing)")

st.write("---")
with st.container():
    st.write("###")
    text_column , image_column = st.columns((2,1))
    with text_column: 
        st.header(":orange[MATH] [TUE/THUR] 10AM - 11:15AM")
        st.write("MATH 2418 Linear Algebra Introduces and provides models for application of the concepts of vector algebra. Topics include finite dimensional vector spaces and their geometric significance; representing, solving systems of linear equations using multiple methods, including Gaussian elimination and matrix inversion; matrices; determinants; linear transformations; quadratic forms; eigenvalues and eigenvectors; and applications in science and engineering.")
        st.subheader(":globe_with_meridians: :blue[***location***] SLC 2.304")
        st.markdown(":orange[**THE TEXTBOOK:**][ TEXTBOOK LINK >](https://drive.google.com/file/d/1DD2kvlITKrs9mDQDAf0mwgrVS-hsJjTh/view?usp=sharing)")
    with image_column:
        st.image(img_contact_math)

st.write("---")
with st.container():
    st.write("###")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_CS)
    with text_column: 
        st.header(":orange[DISCRETE MATH FOR COMPUTING I] [TUE/THUR] 4PM - 5:15PM")
        st.write(" CS 2305 Discrete Mathematics for Computing I Principles of counting. Boolean operations. Logic and proof methods. Recurrence relations. Sets, relations, functions. Elementary graph theory. Elementary number theory.")
        st.subheader(":globe_with_meridians: :blue[***location***] ECSS 2.415")
        st.markdown(":orange[**THE TEXTBOOK:**][ TEXTBOOK LINK >](https://drive.google.com/file/d/1hN-pEjnZmNJSiUujncKiZygqRgZLa0_4/view?usp=sharing)")

st.write("---")
with st.container():
    st.write("###")
    text_column , image_column = st.columns((2,1))
    with text_column: 
        st.header(":orange[UNDERSTANDING FILM] [WED] 4PM - 6:45PM")
        st.write("FILM 2332 Understanding Film Explores the history and stylistic elements of cinema as a mass medium and an art form. The course analyzes visual language and film style, cinematic codes, and the ways that films can embody or criticize popular ideas and attitudes.Emphasis is on film analysis, film in relation to the other arts and mass media, films as artifacts, and understanding the ways that films are put together and how they function expressively.")
        st.subheader(":globe_with_meridians: :blue[***location***] AH2 1.204")
        st.markdown(":orange[**THE TEXTBOOK:**][ TEXTBOOK LINK >](https://drive.google.com/file/d/1IQzrXatiG5QRpbgkesuMF1gn9QDWIb0U/view?usp=sharing)")
    with image_column:
        st.image(img_contact_film)