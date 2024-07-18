import streamlit as st
from about import about_page
from products_services import products_services_page
from job_roles import job_roles_page
from team_builder import team_builder_page

# Set the page configuration
st.set_page_config(page_title="Connext Global Solutions", page_icon="🌐", layout="wide")

# Create a custom sidebar with a navigation menu
with st.sidebar:
    st.markdown("<h2 style='color: #2E2E2E;'>Main Menu</h2>", unsafe_allow_html=True)
    
    menu = {
        "Home": "🏠 Home",
        "About Us": "ℹ️ About Us",
        "Products and Services": "💼 Products and Services",
        "Job Role Requirements": "📋 Job Role Requirements"
    }
    
    page = st.radio("", list(menu.keys()), format_func=lambda x: menu[x])

    st.markdown("""
        <style>
            .stRadio > label {
                font-size: 18px;
                color: #2E2E2E;
                font-weight: bold;
            }
            .stRadio > div {
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #2E2E2E;
            }
            .stRadio input:checked + div {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

# Page Navigation
if page == "Home":
    team_builder_page()
elif page == "About Us":
    about_page()
elif page == "Products and Services":
    products_services_page()
elif page == "Job Role Requirements":
    job_roles_page()
