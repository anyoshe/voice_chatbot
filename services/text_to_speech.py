from gtts import gTTS

def convert_text_to_audio(text, output_file="response.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)
    return output_file
