import streamlit as st

def contact_form():
    st.title("Contact 💼")
    st.write("---")
    st.write("Connect with me on social media:")

    # Social media links
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

    st.write("Use the form below to get in touch:")
    with st.form(key="contact_form"):
        your_name = st.text_input("Your Name")
        your_email = st.text_input("Your Email")
        your_message = st.text_area("Your Message", height=150)
        submit_button = st.form_submit_button("Send")

        if submit_button:
            if your_name and your_email and your_message:
                st.success("Message sent successfully!")
                # Here you can add logic to send email to your Gmail
                # Replace this with actual email sending logic
            else:
                st.error("Please fill out all fields.")

