# import streamlit as st

# def experience():
#     st.title("Industry Experience")
#     st.subheader("Brief Overview")

#     # Define the slider to switch between overview and internship details
#     slide = st.slider("Slide", 1, 2)

#     if slide == 1:
#         # First slide: Title and Overview
#         st.markdown("""
#         ## Sarvesh Udapurkar - Industry Experience
        
#         Sarvesh Udapurkar is a recent graduate with a Bachelor of Engineering in Computer Science 
#         from P. R. Pote College of Engineering and Management, achieving a CGPA of 9.28 (82.58% Aggregate).
        
#         Throughout his academic career, Sarvesh has demonstrated strong academic performance, 
#         excelling in both technical and soft skills. He is proficient in leadership, communication,
#         self-motivation, and graphic design using Canva and MS-Office. Sarvesh has specialized 
#         expertise in the GenAI Tech Stack, including LangChain, HuggingFace, and Retrieval Augmentation
#         Generation (RAG).
        
#         Sarvesh actively participates in extracurricular activities, including serving as a Class Representative 
#         at PRPCEM and completing the Google Bard Generative AI Masterclass certification course on Udemy.
#         """)
#     elif slide == 2:
#         # Second slide: Internship Experience at TCS
#         st.subheader("Internship Experience at Tata Consultancy Services (TCS)")

#         # Create a layout with two columns
#         col1, col2 = st.columns([1, 2])

#         # Column 1: TCS Logo
#         with col1:
#             st.image("tcs_logo.png", caption='TCS Logo', use_column_width=True)

#         # Column 2: Internship Experience Details
#         with col2:
#             st.markdown("""
#             Sarvesh Udapurkar is currently interning at Tata Consultancy Services (TCS), where he is involved
#             in impactful projects:
            
#             - **Proof of Concept (POC) for OpenScenario for ADAS Applications:**
#               - Developed scenarios (Pedestrian and FEB) using XML coding and ASAM tags.
#               - Applied Deep Learning, Machine Learning, Prompting Principles, and Vector Databases.
            
#             - **User Interface (UI) Design for ADAS HILs Automation Framework:**
#               - Designed frontend using Python, demonstrating strong skills in UI development.
            
#             Sarvesh's internship experience at TCS has strengthened his technical skills and provided practical 
#             insights into applying AI and machine learning technologies in real-world projects.
#             """)

# if __name__ == "__main__":
#     experience()



import streamlit as st

def experience():
    st.title("Industry Experience")
    st.write("---")
    # st.subheader("Brief Overview")

    # Define the radio buttons to switch between overview and internship details
    option = st.radio("Select a view:", ('Overview', 'Internship Experience at TCS'))

    if option == 'Overview':
        st.markdown("""
        ## Intern in Tata Consultancy Services (TCS)
        
        I have gained expertise in the GenAI Tech Stack, including LangChain, HuggingFace, and Retrieval Augmentation
        Generation (RAG), Prompting Priciples.

        I have deeply learned about the Machine Learning, Deep Learning and Natural Language Processing Concepts which 
        is play a significant role in development as well as deployment of projects.

        I have Build 4 GenerativeAI based Projects:(RAG - Retieval Augmentation Generation)
        1. Image Researcher - It help in Content Extraction and Generation for Social Media Marketing and there are many realtime use cases of it.
        2. Q&A on PDF - It help in Content Extraction and Generation customized data on Multiple pdf's and context written in the entire PDFs can be questioned and response will get generate.
        3. Excel SQL Retrivel - It help in Content Extraction and Generation on customized data on CSV's, it help findout the exact data you need to extract from the entire csv. 
        It is most accurate as simple sentence get converts in sql query and it will show the entire result based on the data and the sentence that you'll need put.
        4. New Article Generator - It help you to create a Article or Blog kind of content with all the summarized form with titles, keypoints, overview along with references.
        
        
        """)
    elif option == 'Internship Experience at TCS':
        st.subheader("Internship Experience at Tata Consultancy Services (TCS)")

        # Create a layout with two columns
        col1, col2 = st.columns([1, 2])

        # Column 1: TCS Logo
        with col1:
            st.image("https://th.bing.com/th/id/OIP.lLbJ90gEKmzpE3f7nMUrAgAAAA?rs=1&pid=ImgDetMain", caption='TCS Logo', use_column_width=True)

        # Column 2: Internship Experience Details
        with col2:
            st.markdown("""
            Intern in Tata Consultancy Services (TCS)
            Involved in GenerativeAI and OpenScenario 
            - *Proof of Concept (POC) for OpenScenario for ADAS Applications:*
              -----------------------------------------------------------------------------------------
              - Developed scenarios (Pedestrian and FEB) using XML coding and ASAM tags.
              - Applied Deep Learning, Machine Learning, Prompting Principles, and Vector Databases.
              -----------------------------------------------------------------------------------------
            - **User Interface (UI) Design for ADAS HILs Automation Framework:**
              - Designed frontend using Python, demonstrating strong skills in UI development.
              -----------------------------------------------------------------------------------------
            
            Sarvesh's internship experience at TCS has strengthened his technical skills and provided practical 
            insights into applying AI and machine learning technologies in real-world projects.
            """)

if __name__ == "__main__":
    experience()
