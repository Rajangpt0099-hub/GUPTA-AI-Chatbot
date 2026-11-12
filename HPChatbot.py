
import streamlit as st
import google.generativeai as genai

#Initial Gemini Pro
try:
    genai.configure(api_key="AQ.Ab8RN6KSP8K4Hwr38E3drvCzw53QllvMTcoTI57HlKUSzjvcCg")
    model = genai.GenerativeModel('gemini-3.6-flash')
except Exception as e:
    st.error(f"An error occurred while initializing the Gemini API: {e}")

# Gemini uses 'model' for assitant; streamlit uses'assitant'
def role_to_streamlit(role):
    if role =="model":
        return "assistant"
    else:
        return role

#Add a Gemini chat hstory object to streamlit sesson state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

#Display from title
st.title("Chat with GUPTA")
html_temp = """
<div style = "background-color:red;padding:5px">
<h2 style = "color:Black;text-align:center;font-weigth:bold;">Welcome to My chatbot</h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)


# Display chat messages from history above current input box
if "chat" in st.session_state:
    for message in st.session_state.chat.history:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)


# ---------------- FILE UPLOAD FEATURE ----------------

uploaded_file = st.file_uploader(
    "Upload your document or image",
    type=["pdf", "txt", "docx", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Analyze Uploaded File"):

        file_extension = uploaded_file.name.split(".")[-1].lower()

        try:

            # IMAGE FILES
            if file_extension in ["png", "jpg", "jpeg"]:

                import PIL.Image

                image = PIL.Image.open(uploaded_file)

                prompt = [
                    "Analyze this image and explain its contents.",
                    image
                ]

            # PDF FILES
            elif file_extension == "pdf":

                import PyPDF2

                pdf_reader = PyPDF2.PdfReader(uploaded_file)

                pdf_text = ""

                for page in pdf_reader.pages:
                    pdf_text += page.extract_text() or ""

                prompt = f"""
                Analyze the following PDF document and answer questions about it:

                {pdf_text}
                """

            # TEXT FILES
            elif file_extension == "txt":

                pdf_text = uploaded_file.read().decode("utf-8")

                prompt = f"""
                Analyze the following text document:

                {pdf_text}
                """

            # WORD DOCUMENTS
            elif file_extension == "docx":

                from docx import Document

                doc = Document(uploaded_file)

                doc_text = "\n".join(
                    paragraph.text for paragraph in doc.paragraphs
                )

                prompt = f"""
                Analyze the following Word document:

                {doc_text}
                """

            # SEND FILE TO GEMINI
            response = st.session_state.chat.send_message(prompt)

            with st.chat_message("assistant"):
                st.markdown(response.text)

        except Exception as e:
            st.error(f"Error processing file: {e}")


#Aceept users next message ,add to context,resubmit context to gemini
if prompt := st.chat_input("Talk to me about anything"):

    #display users last message
    st.chat_message("user").markdown(prompt)

    #send user entry to gemini and read the response
    response = st.session_state.chat.send_message(prompt)

    #display last
    with st.chat_message("assistant"):
        st.markdown(response.text)
