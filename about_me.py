import streamlit as st

def about_me():
    # Create a layout with two columns
    col1, col2 = st.columns([1, 3])

    # Column 1: Display the image on the left side in a circular manner with a professional border
    with col1:
        st.image("Sarvesh_Udapurkar1.png", 
                 caption="Sarvesh Udapurkar", 
                 width=180, use_column_width=False, output_format='PNG', )
        st.markdown("""
        <div class="social-icons-container">
            <a href="https://www.linkedin.com/in/sarvesh-udapurkar-30a6a4196/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" class="social-icon" alt="LinkedIn">
            </a>
            <a href="https://github.com/sarveshjain2002" target="_blank">
                <img src="https://cdn.jim-nielsen.com/macos/128/github-desktop-2021-05-20.png" class="social-icon" alt="GitHub">
            </a>
            <a href="mailto:udapurkarsarvesh@gmail.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" class="social-icon" alt="Gmail">
            </a>
        </div>
        """, unsafe_allow_html=True)

    # Column 2: Display the text content on the right side
    with col2:
        st.write("""
        Hi, I'm Sarvesh Udapurkar, a recent graduate with a Bachelor of Engineering in Computer Science 
        from P. R. Pote College of Engineering and Management (CGPA: 9.28, Aggregate: 82.58%).
        Throughout my academic career, I have demonstrated strong academic performance, achieving 
        a 68.15% in HSC (Ushabai Deshmukh Junior College) and an 84.00% in SSC (Gurukul Public School).

        I possess a well-rounded skillset encompassing both technical and soft skills. I am proficient 
        in leadership, communication, and self-motivation. Additionally, I am skilled in graphic design 
        using Canva and MS-Office. Notably, I have gained expertise in the GenAI Tech Stack, including 
        LangChain, HuggingFace, and Retrieval Augmentation Generation (RAG).
        """)

        st.subheader("Professional Experience")
        st.markdown("""
        Recently, I have completed internship at Tata Consultancy Services (TCS) where I have been involved 
        in several projects. Here are some highlights:
        - Developed Proof of Concept (POC) for OpenScenario for ADAS applications, creating scenarios using XML coding and ASAM tags.
        - Applied Deep Learning, Machine Learning, Prompting Principles, and Vector Databases in various projects.
        - Developed four Generative AI projects utilizing Open Source APIs like Google Gemini and OpenAI.
            A. Build 4 GenerativeAI based Projects:(RAG - Retieval Augmentation Generation)
            1. Image Researcher - It help in Content Extraction and Generation for Social Media Marketing and there are many realtime use cases of it.
            2. Q&A on PDF - It help in Content Extraction and Generation customized data on Multiple pdf's and context written in the entire PDFs can be questioned and response will get generate.
            3. Excel SQL Retrivel - It help in Content Extraction and Generation on customized data on CSV's, it help findout the exact data you need to extract from the entire csv. 
            It is most accurate as simple sentence get converts in sql query and it will show the entire result based on the data and the sentence that you'll need put.
            4. New Article Generator - It help you to create a Article or Blog kind of content with all the summarized form with titles, keypoints, overview along with references.    
        - Designed the User Interface (UI) for ADAS HILs Automation Framework using Python for frontend development.
        """)

        st.subheader("Key Points")
        st.markdown("""
        <table>
            <tr>
                <td>🌟 <b>Tech Enthusiast</b></td>
                <td>Passionate about Cloud ☁️, Security 🔒, and AI 🤖</td>
            </tr>
            <tr>
                <td>🎓 <b>Solid IT Background</b></td>
                <td>Thrives on tackling challenges and discovering innovative solutions</td>
            </tr>
            <tr>
                <td>🚀 <b>Team Player</b></td>
                <td>Loves participating in hackathons and developer clubs</td>
            </tr>
            <tr>
                <td>💼 <b>Professional Focus</b></td>
                <td>Specializes in Cybersecurity and AI development</td>
            </tr>
            <tr>
                <td>⚽ <b>Outside Tech</b></td>
                <td>Enjoys playing football, trekking ⛰️, hitting the gym 💪, and exploring good food 🍴</td>
            </tr>
            <tr>
                <td>🌱 <b>Life Philosophy</b></td>
                <td>Believes in maintaining a healthy work-life balance for inspiration and productivity</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

        
if __name__ == "__main__":
    about_me()
