import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="Nandini Srivastava | Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills Visualization"])

# Home Page
if page == "Home":
    st.title("Nandini Srivastava")
    st.subheader("Cloud Computing | DevOps | AI Enthusiast")
    st.image("https://avatars.githubusercontent.com/u/12345678?v=4", width=250)
    st.write(
        "Passionate about cloud computing, automation, and AI-driven solutions. Constantly exploring innovative technologies to create scalable digital solutions."
    )
    st.markdown("---")
    
    # Skills Overview
    st.subheader("Skills")
    skills = {"Cloud Computing": 90, "Docker": 85, "Kubernetes": 75, "Python": 80, "Machine Learning": 70}
    for skill, level in skills.items():
        st.progress(level / 100)
        st.text(f"{skill}: {level}%")

# Projects Page
elif page == "Projects":
    st.title("Featured Projects")
    project_data = {
        "Project Name": ["Classroom Vacancy System", "Mushroom Classification App", "Dockerized ML Model"],
        "Description": [
            "An intelligent system to manage classroom allocations.",
            "A Streamlit app for classifying mushroom species using ML.",
            "An ML model wrapped inside a Dockerized Streamlit app."
        ],
        "GitHub": [
            "https://github.com/user/classroom-system",
            "https://github.com/user/mushroom-app",
            "https://github.com/user/docker-ml"
        ]
    }
    df_projects = pd.DataFrame(project_data)
    st.table(df_projects)

# Skills Visualization
elif page == "Skills Visualization":
    st.title("Technical Skills Distribution")
    skill_labels = list(skills.keys())
    skill_values = list(skills.values())
    
    fig, ax = plt.subplots()
    ax.barh(skill_labels, skill_values, color='skyblue')
    ax.set_xlabel("Proficiency (%)")
    ax.set_title("Skill Set Overview")
    st.pyplot(fig)
    
    st.write("This chart represents my proficiency levels in different technical domains.")

st.sidebar.info("Check out my Streamlit profile: [Click Here](https://share.streamlit.io/user/nandinisrivastava)")
