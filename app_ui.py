import streamlit as st
import requests

# FastAPI Backend chi URL
BACKEND_URL = "http://127.0.0.1:8000/students"

st.set_page_config(page_title="Student Record System", layout="centered")

st.title("🎓 Student Information System")
st.write("Fill the details below to add a student to the database.")

# 1. 'Create' Button check karnyathi state vapru
if "show_form" not in st.session_state:
    st.session_state.show_form = False

# 'Create Student' Button
if st.button("➕ Create New Student"):
    st.session_state.show_form = True

# 2. Form open hoil jeva 'Create' click hoil
if st.session_state.show_form:
    with st.form("student_form", clear_on_submit=True):
        st.subheader("Enter Student Details")
        
        roll_no = st.number_input("Roll Number", min_value=1, step=1)
        name = st.text_input("Student Name")
        std = st.number_input("Standard (Std)", min_value=1, max_value=12, step=1)
        marks = st.number_input("Marks", min_value=0.0, max_value=100.0)

        submit_button = st.form_submit_button("Submit to Backend")

        if submit_button:
            if name:
                # Backend API la data pathvne (POST Request)
                data = {
                    "rollNo": roll_no,
                    "name": name,
                    "std": std,
                    "marks": marks
                }
                
                try:
                    # Query parameters dware data pathvtat (FastAPI logic nusar)
                    response = requests.post(
                        f"{BACKEND_URL}?rollNo={roll_no}&name={name}&std={std}&marks={marks}"
                    )
                    
                    if response.status_code == 200:
                        st.success(f"✅ Success: {name} cha data save jhala!")
                        st.session_state.show_form = False # Form hide kara
                    else:
                        st.error("❌ Error: Data save hou shakla nahi.")
                except Exception as e:
                    st.error(f"❌ Connection Failed: Backend chalu aahe ka? {e}")
            else:
                st.warning("⚠️ Krupaya student che naav taka.")