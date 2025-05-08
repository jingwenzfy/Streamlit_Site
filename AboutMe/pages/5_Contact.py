import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Contact | Jingwen Zhang", page_icon="📬")

st.title("Feel free to get in touch!")

st.markdown("""


📧 **Email**: [jingwenz@berkeley.edu](mailto:jingwenz@berkeley.edu)
            
📱 **Phone**: +1 (949) 664-9129
            
🔗 **LinkedIn**: [linkedin.com/in/jingwen-zhang22](https://www.linkedin.com/in/jingwen-zhang22)
            
📍 **Current Location**: Berkeley, CA

---

Alternatively, you can send me a message directly here:
""")

# Contact form
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    sender_email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")

    if submit:
        if name and sender_email and message:
            try:
                # Compose email
                email = EmailMessage()
                email['Subject'] = f"New Stramlit Contact Form Message from {name}"
                email['From'] = st.secrets["email_user"]
                email['To'] = st.secrets["email_to"]
                email.set_content(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}")

                # Send email
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(st.secrets["email_user"], st.secrets["email_pass"])
                    smtp.send_message(email)

                st.success("Thanks for reaching out! Your message has been sent. 😊")

            except Exception as e:
                st.error(f"Something went wrong. Error: {e}")
        else:
            st.error("Please fill in all fields before submitting.")
