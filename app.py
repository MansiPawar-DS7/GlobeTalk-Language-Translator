import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS


st.title("🌍 GlobeTalk : Language Translator")


# language option

language = {

    "English" : "en",
    "Hindi" : "hi",
    "Marathi" : "mr",
    "German" : "de",
    "Spanish" : "es",
    "French" : "fr",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Japanese" : "ja",
    "Russian" : "ru",
    "Portuguese" : "pt",
    "Arabic" : "ar",
    "Italian" : "it",
    "Korean" : "ko",
    "Dutch" : "nl",
    "Gujarati" : "gu",
    "Kannada" : "kn",
    "Malayalam" : "ml",
    "Bengali" : "bn",
    "Telugu" : "te",
    "Punjabi" : "pa",
    "Urdu" : "ur",
    "Tamil" : "ta",
    "Swedish" : "sv",
    "Finnish" : "fi",
    "Norwegian" : "no",
    "Polish" : "pl",
    "Mongolian": "mn",
    "Myanmar": "my",
    "Nepali": "ne",
    "Romanian": "ro",
    "Sanskrit": "sa",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Thai": "th"

}


# dropdown

source_lang = st.selectbox(
    "Translate from",
    language.keys()
)


target_lang = st.selectbox(
    "Translate to",
    language.keys()
)



# input text

text = st.text_area(
    "Enter your text :)"
)



# Translate button

if st.button("🚀 Translate"):


    translated = GoogleTranslator(

        source=language[source_lang],

        target=language[target_lang]

    ).translate(text)



    # save translation

    st.session_state.translation = translated


   # st.success("Translation:")

   # st.write(translated)

# Show translation always

if "translation" in st.session_state:

    st.success("Translation:")

    st.write(st.session_state.translation)


# Text to Speech

if "translation" in st.session_state:


    if st.button("🔊 Listen"):


        audio = gTTS(

            text=st.session_state.translation,

            lang=language[target_lang]

        )


        audio.save("voice.mp3")


        st.audio("voice.mp3")