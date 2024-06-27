import streamlit as st

def technical():
    st.title("Technical Skills and Projects 💻")
    st.write("---")
    
    # Define project details
    project = {
        "title": "1. Image Researcher",
        "technologies": "LangChain, Google Gemini Vision Pro",
        "deployment_link": "https://imageresearcher.streamlit.app/",
        "video_path": "Proof_Image.webm",
        # "image_path": "D:/A FULL ENGINEERING DATA/1.GenAI/Portfolio_Gemini_/Images/image_researcher.png"
    }
    
    # Project details (Title, Technologies, Deployment Link)
    st.markdown(f"## {project['title']}")
    st.markdown(f"**Technologies Used:** {project['technologies']}")
    st.markdown(f"**Deployed Link:** [{project['deployment_link']}]({project['deployment_link']})")
    
    # Display video using st.video()
    st.video(project['video_path'], start_time=0, format='AI Powered Portfolio/video/webm', autoplay=True)
    
if __name__ == "__main__":
    technical()
