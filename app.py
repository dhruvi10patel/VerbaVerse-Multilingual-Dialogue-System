from dotenv import load_dotenv
import streamlit as st
import os
from googletrans import Translator
import google.generativeai as genai
from PIL import Image
from streamlit_extras import add_vertical_space as avs 

load_dotenv()  

# Configure the GenerativeAI module
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(question, language="en"):
    translator = Translator()
    question_translated = translator.translate(question, dest=language).text
    response = model.generate_content(question_translated)
    return response.text


# Streamlit UI
st.set_page_config(page_title="Multilingual Chatbot")
# Header with custom font style
st.title("VerbaVerse")
st.header("Your Multilingual Dialogue Dynamo")
st.markdown("""<p style='text-align: justify;'>
                Welcome to VerbaVerse! Our platform enables seamless multilingual communication, allowing users to engage in conversations and 
                receive responses effortlessly across languages. Whether it's personal or professional, VerbaVerse fosters clear communication 
                and global connectivity. Join us today to unlock the power of multilingual dialogue!
                </p>""", unsafe_allow_html=True)

img = Image.open("images/icon.png")
col1, col2, col3 = st.columns([1, 3, 1])  
with col2:
    st.image(img, use_column_width=True)

st.header("What we Offer?")

col1, col2 = st.columns([1, 3])  
with col1:
    img1 = Image.open("images/icon1.png")
    st.image(img1, width=150)
    
with col2:
    st.markdown("""<p style='text-align: justify;'><b>Multilingual Customer Support: </b>
                VerbaVerse offers multilingual assistance for troubleshooting, product inquiries, and general support, ensuring a 
                smooth customer experience across languages.
                </p>""", unsafe_allow_html=True)

avs.add_vertical_space(4)

col1, col2 = st.columns([1, 3])  
with col1:
    img2 = Image.open("images/icon2.png")
    st.image(img2, width=150)
    
with col2:
    st.markdown("""<p style='text-align: justify;'><b>Language Learning and Practice: </b>
                Users can practice and improve language skills by engaging in conversations with the chatbot, receiving real-time 
                feedback, and accessing learning resources, fostering proficiency and confidence.
                </p>""", unsafe_allow_html=True)

avs.add_vertical_space(4)

col1, col2 = st.columns([1, 3])  
with col1:
    img3 = Image.open("images/icon3.png")
    st.image(img3, width=150)
    
with col2:
    st.markdown("""<p style='text-align: justify;'><b>Multilingual Content Translation and Summarization: </b>
                VerbaVerse provides accurate translation and concise summarization of documents, articles, and textual data in 
                multiple languages, facilitating efficient information processing and analysis.
                </p>""", unsafe_allow_html=True)


avs.add_vertical_space(4)

st.markdown("<h1 style='text-align: center;'>Let's Engage</h1>", unsafe_allow_html=True)
img4 = Image.open("images/bot.png")
st.image(img4, use_column_width=True)
input_text = st.text_input("Input: ", key="input")

# Dropdown for selecting language
selected_language = st.selectbox("Select Language:", options=["Arabic", "Bengali", "Chinese", "Dutch", "English",
                                                             "French", "German", "Greek", "Hindi", "Italian",
                                                             "Japanese", "Korean", "Polish", "Portuguese",
                                                             "Russian", "Spanish", "Swedish", "Turkish", "Urdu"])


# Map language names to language codes
language_map = {
    "Arabic": "ar",
    "Bengali": "bn",
    "Chinese": "zh-CN",
    "Dutch": "nl",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Polish": "pl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Spanish": "es",
    "Swedish": "sv",
    "Turkish": "tr",
    "Urdu": "ur"
} 

# Convert selected language to language code
language_code = language_map.get(selected_language, "en")

# Button to ask the question
submit_button = st.button("Ask the Question")

# When submit button is clicked
if submit_button:
    response = get_gemini_response(input_text, language=language_code)
    st.write(response)

st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True)
st.info("""What languages does VerbaVerse support for customer support? \n 
        VerbaVerse supports a wide range of languages, ensuring efficient 
    assistance for users regardless of their preferred language.""")
st.info("""Can VerbaVerse provide real-time feedback on language usage during practice sessions? \n 
        Yes, VerbaVerse offers real-time feedback on grammar and vocabulary 
    usage, helping users improve their language skills effectively.""")
st.info("""Is VerbaVerse suitable for professionals dealing with multilingual content? \n 
        Absolutely! VerbaVerse is designed to meet the needs of professionals, 
    enabling efficient information processing and analysis across language 
    barriers.""")

