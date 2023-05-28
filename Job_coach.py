import datetime
import csv 
import numpy as np
import streamlit as st
import mysql.connector as mc

#CREATING CONNECTION BETWEEN PYTHON AND MYSQL
conn = mc.connect(host = "localhost", user = "root", password = "shaatvika219", database = "company_data")
cur = conn.cursor()

#GUI 
st.title('JOB COACH')

tab1,tab2 = st.tabs(["Personal Information","Job Recommendation"])

with tab1:

    name = st.text_input("Name")
    age = st.text_input("Age")
    dob = st.date_input(
        "When's your birthday",
            datetime.date(2002,1,1))
    gender = st.radio("Gender",
                 ('Male', 'Female'))
    ph_no = st.text_input("Phone number")
    email_id = st.text_input("Email ID")
    address = st.text_area("Address")
    nationality = st.radio("Nationality",
                        ('Indian','NRI','OCI'))
    
    st.write("2. QUALIFICATIONS")
    st.write("10th STANDARD")
    st.number_input("Marks (Enter percentage)")
    st.write("12th standard")
    st.number_input(" Marks (Enter percentage)", key = 12)
        
    degree = st.selectbox(
        'Degree',
        ('BTECH', 'Msc', 'Bsc'))
    cgpa_range = st.radio("Enter your CGPA range",
            ("<7","7-8","8-9",">9"))
    cgpa = st.slider('Select your exact CGPA', 0.0, 10.0, 7.0)
    uploaded_files = st.file_uploader("Upload 10th, 12th and degree certificates", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        st.write("Filename:", uploaded_file.name)
       
    internships = st.radio("Enter no.of internships",
            ("<1","1-2",">2"))
    st.write("Select known coding languages")
    
    lang_1 = st.checkbox("Python")
    lang_2 = st.checkbox("C")
    lang_3 = st.checkbox("Java")
    lang_4 = st.checkbox("Linux (shell coding)")
    lang_5 = st.checkbox("Select if known language not in list")
    lang_known = lang_1+lang_2+lang_3+lang_4+lang_5
    

    certificate_courses = st.number_input("Enter no of certificates uploaded",key = int)

    
    upload_file = st.file_uploader("Upload certificates of courses/ competitions participated", accept_multiple_files=True)
    certi_count = 0
    for uploaded_file in upload_file:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
          
        certi_count+=1
    
    st.write("4. JOB SPECIFICATIONS:")
    area1 = st.selectbox(
       "Select your first preferred location",
       ["Bengaluru","Mumbai","Pune","Delhi","Hyderabad","Chennai","Kolkata"])
    area2 = st.selectbox(
        "Select your second preferred location", #The option selected in area 1 will be  removed
        ["Bengaluru","Mumbai","Pune","Delhi","Hyderabad","Chennai","Kolkata"])
    area3 = st.selectbox("Select your third preferred location", #The option selected in area 1 and area2 will be  removed
        ["Bengaluru","Mumbai","Pune","Delhi","Hyderabad","Chennai","Kolkata"]) 
    area_list = [area1,area2,area3]
    
    mode_of_work = st.radio('Select your preferred mode of work',
                       ('Offline','Online','Hybrid'))
    salary = st.slider("Expected salary (in Lakhs per annum)", 6.0, 70.0, (7.5,8.0))
    upload_files = st.file_uploader("Upload you photo and signature", accept_multiple_files=True)
    for uploaded_file in upload_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        
    fields = ["Name","Age","DOB","Gender","Phone_number","EmailId","Address","Nationality","Degree"]

    if st.button("Submit"):
        if name and age and degree and cgpa and internships and lang_known !=  None:
            file_name = "User Information.csv"
            data_input = [name,age,dob,gender,ph_no,email_id,address,nationality,degree]
            with open(file_name,'a') as csv_file:
            #with open(file_name,'w') as csv_file:
                writer = csv.writer(csv_file)
                #writer.writerow(fields)
                writer.writerow(data_input)
                st.write("Please click on the Job recommendations tab to view your result")
    
        elif certi_count != certificate_courses:
            st.warning("Please upload correct number of certificates")
            
        else:
            st.warning("Please fill all required fields")
            

#LOGIC_CODING
basic = dreamers = super_dream = 0

#SEGREGEATION BASED ON CGPA
#float_range generator
# range for floats with np.arange()
if cgpa < 6.0:
    basic+=1
elif cgpa in np.arange(6.1,8.6,0.1):
    dreamers+=1
elif cgpa in np.arange(8.6,10.1,0.1):
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
if internships == ">1":
    basic+=1
elif internships == "1-2":
    dreamers += 1
elif internships == ">2":
    super_dream+=1

#LANGUAGES KNOWN 
if lang_known <2:
    basic+=1
elif lang_known in range(2,5):
    dreamers+=1
elif lang_known >4:
    super_dream+=1

#CERTIFICATES
if certificate_courses == 0:
    basic+=0
    dreamers+=0
    super_dream+=0

elif certificate_courses <2:
    basic+=1
elif  certificate_courses in range(2,5):
    dreamers+=1
elif certificate_courses >4:
    super_dream+=1

determination_list = [basic,dreamers,super_dream]
max_count = max(determination_list)

#Company dictionary creation + data printing 
company_dict = {}
if max_count == basic:
    cur.execute("SELECT * FROM basic_package")
    li = cur.fetchall()
    #print(li)
    list_temporary = li
        
    for i in list_temporary:
        city = i[4]
        x = list(i)
        x.pop(4)
            
        if city not in company_dict:
            company_dict[city] = []
        company_dict[city].append(x)


if max_count == dreamers:
    cur.execute("SELECT * FROM dream_companies")
    li = cur.fetchall()
    #print(li)
    list_temporary = li
    
    for i in list_temporary:
        city = i[4]
        x = list(i)
        x.pop(4)
            
        if city not in company_dict:
            company_dict[city] = []
        company_dict[city].append(x)


if max_count == super_dream:
    cur.execute("SELECT * FROM superdream_companies")
    li = cur.fetchall()
    #print(li)
    list_temporary = li
    
    for i in list_temporary:
        city = i[4]
        x = list(i)
        x.pop(4)
            
        if city not in company_dict:
            company_dict[city] = []
        company_dict[city].append(x)
l = list(company_dict.keys())
company = company_dict

#OUTPUT PAGE 
with tab2:
    st.header("JOB RECOMMEDATIONS")
    st.write("Based on your given data, these are the suitable jobs available in your preferred cities:")
    for i in area_list:
        
        st.header(i)
        if i not in company:
            st.write("No company in preferred location")
            continue

        else:
            for j in company[i]:
                
                st.subheader("__Company name:__")
                st.write(j[1])
                st.subheader("__About:__")
                st.write(j[3])
                st.subheader("__Expected Salary:__")
                st.write(j[2])
                st.subheader("__Branch location(s):__")
                st.write(j[4])
                st.subheader("__Contact details:__")
                st.write(j[5])
                st.subheader("__Email id:__")
                st.write(j[6])
        del company[i]
    
    st.write("Similar Companies in other locations: ")
    for a in company:
        st.header(a)
        for b in company[a]:
            st.subheader("__Company name:__")
            st.write(b[1])
            st.subheader("__About:__")
            st.write(b[3])
            st.subheader("__Expected Salary:__")
            st.write(b[2])
            st.subheader("__Branch location(s):__")
            st.write(b[4])
            st.subheader("__Contact details:__")
            st.write(b[5])
            st.subheader("__Email id:__")
            st.write(b[6])
    
