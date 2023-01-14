#st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, 
#on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
import datetime

import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO 


st.title('JOB COACH')

tab1,tab2 = st.tabs(["Personal Information","Job Recommendation"])

with tab1:

    name = st.text_input("Name","Enter your name")
    age = st.text_input("Age","Enter your age")
    dob = st.date_input(
        "When's your birthday",
            datetime.date(2002,1,1))
    gender = st.radio("Gender",
                 ('Male', 'Female'))
    ph_no = st.number_input("Phone number",key = int)
    email_id = st.text_input("Email ID","Enter your official email id")
    address = st.text_area("Address","Enter your current residential address")
    nationality = st.radio("Nationality",
                        ('Indian','NRI','OCI'))
    st.download_button('Download Sample Text',f"{name}\n{age}\n{dob}\n{gender}\n{ph_no}\n{email_id}\n{address}\n{nationality}")
    



    st.write("2. QUALIFICATIONS")
    st.write("10th STANDARD")
    st.number_input("Marks (Enter percentage)")
    marksheet_10 = st.file_uploader("Upload your 10th marksheet")
    if marksheet_10 is not None:
        # To read file as bytes:
        bytes_data = marksheet_10.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(marksheet_10.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(marksheet_10)
        st.write(dataframe)
    st.write("12th standard")
    st.number_input(" Marks (Enter percentage)", key = 12)
    marksheet_12 = st.file_uploader("Choose a file")
    if marksheet_12 is not None:
        # To read file as bytes:
        bytes_data = marksheet_12.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(marksheet_12.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(marksheet_12)
        st.write(dataframe)
    degree = st.selectbox(
        'Degree',
        ('BTECH', 'Msc', 'Bsc'))
    cgpa_range = st.radio("Enter your CGPA range",
            ("<7","7-8","8-9",">9"))
    cgpa = st.slider('Select your exact CGPA', 0.0, 10.0, 7.0)
    degree_certi = st.file_uploader("Upload your degree certificate")
    if degree_certi is not None:
        # To read file as bytes:
        bytes_data = degree_certi.getvalue()
        st.write(bytes_data)

    # To convert to a string based IO:
        stringio = StringIO(degree_certi.getvalue().decode("utf-8"))
        st.write(stringio)
    # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(degree_certi)
        st.write(dataframe)




    st.text_area("Write a few lines about yourself and explain your skill sets"," ")
    extra_skills = st.file_uploader("Upload certificates of extra courses or any competitions won")
    internships = st.radio("Enter no.of internships",
            ("<2","2-5",">5"))
    st.write("Select known coding languages")
    lang_1 = st.checkbox("Python")
    lang_2 = st.checkbox("C")
    lang_3 = st.checkbox("Java")
    lang_4 = st.checkbox("Linux (shell coding)")
    lang_5 = st.checkbox("Select if known language not in list")
    lang_known = lang_1+lang_2+lang_3+lang_4+lang_5
    st.write("Select no of certificate courses attended")
    
    

    
    if extra_skills is not None:
        # To read file as bytes:
        bytes_data = extra_skills.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(extra_skills.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(extra_skills)
        st.write(dataframe)
 
    st.write("4. JOB SPECIFICATIONS:")
    area1 = st.selectbox(
       "Select your first preferred location",
       ["Bangalore","Mumbai","Pune","Delhi","Noida","Hyderabad","Chennai"])
    area2 = st.selectbox(
        "Select your second preferred location", #The option selected in area 1 will be  removed
        ["Bangalore","Mumbai","Pune","Delhi","Noida","Hyderabad","Chennai"])
    area3 = st.selectbox("Select your third preferred location", #The option selected in area 1 and area2 will be  removed
        ["Bangalore","Mumbai","Pune","Delhi","Noida","Hyderabad","Chennai"]) 
    
    mode_of_work = st.radio('Select your preferred mode of work',
                       ('Offline','Online','Hybrid'))
    salary = st.slider("Expected salary (in Lakhs per annum)", 6.0, 70.0, (7.5,8.0))
    uploaded_files = st.file_uploader("Upload you photo and signature", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)  
    st.button("Submit")
basic = dreamers = super_dream = 0

#SEGREGEATION BASED ON CGPA
if cgpa < 6:
    basic+=1
elif cgpa in range (7,8.6):
    dreamers+=1
elif cgpa in range (8.6,10.1):
    super_dream+=1

#DEGREE 
if degree == "Bsc":
    basic+=1
elif degree == "BTECH":
    dreamers+=1
    super_dream+=1
elif degree == "Msc":
    super_dream+=1

#NO OF INTERNSHIPS
if internships == ">2":
    basic+=1
elif internships == "2-5":
    dreamers += 1
elif internships == ">5":
    super_dream+=1

#LANGUAGES KNOWN 
if lang_known <2:
    basic+=1
elif lang_known in range(2,5):
    dreamers+=1
elif lang_known >4:
    super_dream+=1

#Certiicates and internships


with tab2:
    st.write("JOB RECOMMEDATION")
    st.write("Based on your given data, these are the suitable jobs")
