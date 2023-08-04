from flask import Flask, request, jsonify, render_template
from .transcribe import transcribe_audio
from .correct_text import correct_text

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        transcription = transcribe_audio(file)
        corrected_transcription = correct_text(transcription)
        return jsonify({'transcription': corrected_transcription})

if __name__ == '__main__':
    app.run(debug=True)

