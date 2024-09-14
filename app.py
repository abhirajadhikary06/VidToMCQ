from flask import Flask, render_template, request, redirect, url_for
import moviepy.editor as mp
import speech_recognition as sr
import google.generativeai as genai
import os

app = Flask(__name__)

# Ensure a folder for uploaded files exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the Google Generative AI API
genai.configure(api_key=os.getenv("AIzaSyBAms54N5x63d8uxqBAModLo95AcBpGUkA"))  # Use environment variable for API Key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return "No video file part in the request."
    
    video_file = request.files['video']
    
    if video_file.filename == '':
        return "No selected file."
    
    # Save the video file securely
    video_path = os.path.join(UPLOAD_FOLDER, 'uploaded_video.mp4')
    video_file.save(video_path)

    # Extract audio from video
    try:
        video = mp.VideoFileClip(video_path)
        audio_path = os.path.join(UPLOAD_FOLDER, 'audio.wav')
        video.audio.write_audiofile(audio_path)
    except Exception as e:
        return f"Error processing video: {e}"

    # Transcribe the audio
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        return f"Error with audio transcription: {e}"

    # Use Google Generative AI to generate MCQs from the transcribed text
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Generate 5 multiple-choice questions from the following text:\n{text}"
        response = model.generate_content(prompt)
        questions = response.text  # Get the generated questions
    except Exception as e:
        return f"Error with Gemini API: {e}"

    # Split questions by line and return them to the template
    return render_template('result.html', questions=questions.split('\n'))

if __name__ == '__main__':
    app.run(debug=True)
