import streamlit as st

# Define the resume content
def main():
    st.title("Praveen Srikar Vukkum - Resume")

    st.header("Contact Information")
    st.write("**Email:** praveensreekar05@gmail.com")
    st.write("**Phone:** +91 9573055478")
    st.write("**LinkedIn:** [Praveen Srikar Vukkum](https://www.linkedin.com/in/praveensrikarvukkum)")

    st.header("Objective")
    st.write("To obtain a challenging role where I can apply my skills to contribute to the company’s success while also enhancing my knowledge and professional growth.")

    st.header("Education")
    st.write("**Bachelor of Technology in Computer Science and Engineering**")
    st.write("Ramachandra College of Engineering, Eluru")
    st.write("Graduation: 2024 | CGPA: 7.49")
    st.write("**Intermediate**")
    st.write("NRI Junior College, Eluru")
    st.write("Graduation: 2020 | GPA: 6.63")
    st.write("**SSC**")
    st.write("Ravindra Bharathi Public School, Vijayawada")
    st.write("Graduation: 2018 | GPA: 8.0")

    st.header("Technical Skills")
    st.write("- **Programming Languages**: Python, Java, C++, HTML, CSS, JavaScript")
    st.write("- **Database**: SQL (Commands, DDL, DML, DQL)")
    st.write("- **Tools**: Visual Studio, PyCharm, Google Colab, Canva")
    st.write("- **Software**: Microsoft Office (PowerPoint, Excel, Word)")

    st.header("Internships")
    internships = [
        "Cloud Virtual Internship (AWS Academy)",
        "AI-ML Virtual Internship (AWS Academy)",
        "AI-ML Virtual Internship (Google Developers)",
        "Cybersecurity Virtual Internship (Beacon - Palo Alto Networks)",
        "Android Developer Virtual Internship (Google Developers)",
        "Front End Development Internship (IBM Skill Build Program)"
    ]
    for internship in internships:
        st.write(f"- {internship}")

    st.header("Projects")
    st.write("**YogaSana Website** (May 2023 - August 2023)")
    st.write("Developed a platform for yoga instructors to showcase their services and connect with clients.")
    st.write("**Crop Yield Prediction System** (January 2024 - May 2024)")
    st.write("Implemented a Machine Learning model to optimize crop growth and yield based on environmental factors.")

    st.header("Achievements")
    st.write("**3rd Place** - NASA Space Apps Challenge Hackathon (November 2022)")

    st.header("Extracurricular Activities")
    st.write("Organized and managed a Mathematics Expo at Ravindra Bharathi Public School, Eluru (April 2017)")

    st.header("Interests")
    st.write("- Reading puranas")
    st.write("- Solving puzzles")
    st.write("- Browsing industry trends")

    st.header("Strengths")
    st.write("- Quick learning")
    st.write("- Proactive and initiative-taker")
    st.write("- Strong team collaboration skills")

if __name__ == "__main__":
    main()
