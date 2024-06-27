import streamlit as st
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from contact import contact_form
from about_me import about_me
from experience import experience
from education import education
from technical import technical

load_dotenv()

# Function to process PDF and prepare text chunks
def process_pdf(pdf_path):
    if os.path.exists(pdf_path):
        pdf_reader = PdfReader(pdf_path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        chunks = text_splitter.split_text(text)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        return True
    else:
        st.error(f"PDF file not found at path: {pdf_path}")
        return False

# Function to get conversational chain for ChatBot
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Main function to setup Streamlit app
def main():
    st.set_page_config(page_title="Sarvesh's Portfolio", 
                       page_icon="https://avatars.githubusercontent.com/u/93316880?s=400&u=a74eba73422899667076b3326c5104d3fb58bd42&v=4", 
                       layout="wide")

    # Define CSS for navigation tabs, social media icons, and chat messages
    st.markdown(
        """
        <style>
            .sidebar-content {
                padding-top: 20px;
            }
            .sidebar-item {
                padding: 10px 16px;
                margin-bottom: 5px;
                text-align: center;
                font-weight: bold;
                color: #fff;
                border: 1px solid #ccc;
                border-radius: 5px;
                transition: background-color 0.3s;
                font-size: 18px;
            }
            .sidebar-item:hover {
                background-color: #4CAF50;
            }
            .social-icons-container {
                display: flex;
                align-items: center;
                margin-top: 20px;
                margin-bottom: 20px;
            }
            .social-icon {
                margin: 0 10px;
                height: 32px;
                width: 32px;
                cursor: pointer;
                transition: transform 0.3s;
            }
            .social-icon:hover {
                transform: scale(1.1);
            }
            .contact-form {
                margin-top: 20px;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .contact-form input, .contact-form textarea {
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            .contact-form button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            .contact-form button:hover {
                background-color: #45a049;
            }
            .response-text-area {
                resize: vertical;
                height: 300px;
            }
            .cool-content {
                padding: 20px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin-bottom: 20px;
            }
            .chat-message {
                padding: 1rem;
                border-radius: 0.5rem;
                margin-bottom: 1rem;
                display: flex;
                align-items: flex-start;
            }
            .chat-message.user {
                justify-content: flex-end;
                background-color: #2b313e;
            }
            .chat-message.bot {
                background-color: #475063;
            }
            .chat-message .avatar {
                width: 20%;
            }
            .chat-message .avatar img {
                max-width: 78px;
                max-height: 78px;
                border-radius: 50%;
                object-fit: cover;
            }
            .chat-message .message {
                width: 80%;
                padding: 0 1.5rem;
                color: #fff;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar navigation
    st.sidebar.write("---")

    st.sidebar.title("Detailed Info: ")
    # st.sidebar.write("---")

    # Define the navigation buttons
    sidebar_items = ["Home 🔗", "About Me 👨‍💻", "Experience 🎓", "Education🧑‍🎓", "Technical Skills and Projects 💻", "Contact 💼"]
    selected_item = st.sidebar.radio("Navigation :-", sidebar_items)
    st.sidebar.write("---")

    if selected_item == "Home 🔗":
        st.title("Welcome to Sarvesh's Portfolio")
        st.write("---")

        # Initialize ChatBot chain
        chain = get_conversational_chain()

        # Process PDF
        pdf_path = "Sarvesh_Udapurkar_6M_Intern_TCS_GenAI.pdf"
        
        if process_pdf(pdf_path):
            st.write("""
                Greetings, Human! 👋 I'm Gipsy, an AI trained to answer questions about Sarvesh. 
                Curious about his projects, skills, or anything else? Just ask! 😉
            """)

        # Chatbot interface section
        st.write("### Chat with Gipsy 🤖")

        # Handle user input and show response
        user_question = st.text_input("Type your question here", value=st.session_state.get('user_question', ''))
        if st.button("Ask"):
            with st.spinner("Generating Response..."):
                try:
                    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
                    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
                    docs = new_db.similarity_search(user_question)

                    response = chain(
                        {"input_documents": docs, "question": user_question},
                        return_only_outputs=True
                    )

                    bot_template = '''
                    <div class="chat-message bot">
                        <div class="avatar">
                            <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
                        </div>
                        <div class="message">{}</div>
                    </div>
                    '''

                    user_template = '''
                    <div class="chat-message user">
                        <div class="avatar">
                            <img src="https://cdn.technologyadvice.com/wp-content/uploads/2018/02/friendly-chatbot.jpg">
                        </div>    
                        <div class="message">{}</div>
                    </div>
                    '''

                    st.markdown(user_template.format(user_question), unsafe_allow_html=True)
                    st.markdown(bot_template.format(response["output_text"]), unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error in ChatBot interaction: {str(e)}")

    # elif selected_item == "About Me 👨‍💻":
    #     st.title("About Me")
    #     st.write("This is some dummy content for About Me.")
    if selected_item == "About Me 👨‍💻":
        st.title("About Me 👨‍💻")
        st.write("---")
        about_me()

    if selected_item == "Experience 🎓":
        # st.title("Experience")
        experience()
    if selected_item == "Technical Skills and Projects 💻" :
        # st.title("Technical Skills")
        technical()
    if selected_item == "Education🧑‍🎓":
        # st.title("Education")
        education()

        # st.title("Projects")
        # st.write("This is some dummy content for Projects.")

    # elif selected_item =="Achievements ♨️":
    #     st.title("Achievements")
    #     st.write("This is some dummy content for Achievements.")

    if selected_item ==  "Contact 💼":
        contact_form()

if __name__ == "__main__":
    main()
