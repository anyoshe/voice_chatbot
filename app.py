from flask import Flask, request, jsonify
from services.speech_to_text import convert_audio_to_text
from services.language_detect import detect_language
from services.nlp_processor import process_text_with_openai
from services.text_to_speech import convert_text_to_audio

app = Flask(__name__)

@app.route("/process-voice", methods=["POST"])
def process_voice():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    audio_path = f"static/{audio_file.filename}"
    audio_file.save(audio_path)

    # Step 1: Speech-to-Text
    transcript = convert_audio_to_text(audio_path)

    # Step 2: Language Detection
    language = detect_language(transcript)

    # Step 3: NLP Processing
    chatbot_response = process_text_with_openai(transcript)

    # Step 4: Text-to-Speech (optional)
    audio_response_path = convert_text_to_audio(chatbot_response)

    return jsonify({
        "transcript": transcript,
        "language": language,
        "response": chatbot_response,
        "audio_response": audio_response_path
    })

if __name__ == "__main__":
    app.run(debug=True)
