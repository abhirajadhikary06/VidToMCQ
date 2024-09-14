# <span style="font-size: 2em;">VidTOMCQ</span>

**VidTOMCQ** is an AI-powered project that allows users to upload video content and automatically generates 5 multiple-choice questions (MCQs) based on the content of the video. This project integrates speech recognition, video processing, and generative AI to create an innovative tool for learning and assessment.

## Features:
- Extracts audio from user-uploaded video input.
- Transcribes audio content using advanced speech recognition technology.
- Utilizes AI to generate 5 relevant MCQs based on the transcribed content.
- Simple and intuitive web interface for easy video upload and question display.

## Technologies Used:
- **Flask**: Backend web framework to manage routing and handling.
- **MoviePy**: For processing and extracting audio from video.
- **SpeechRecognition**: To transcribe video audio into text.
- **Google Generative AI**: To create meaningful and context-based MCQs from the transcribed text.

## How It Works:
1. The user uploads a video file via the web interface.
2. The system extracts the audio from the video.
3. Speech recognition transcribes the audio into text.
4. Google Generative AI analyzes the text and generates 5 MCQs.
5. The questions are displayed on the results page.

## Installation:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abhirajadhikary06/VidToMCQ.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd VidTOMCQ
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:
    ```bash
    flask run
    ```

## Usage:
1. Access the web interface by navigating to `http://localhost:5000` in your web browser.
2. Upload a video file (supported formats: `.mp4`, `.avi`, etc.).
3. The system processes the video and generates 5 MCQs.
4. View the generated questions on the result page.

## Example Output:
After uploading a video, the system generates questions such as:
1. What was the main topic discussed in the video?
2. Which key point was emphasized in the video?
3. What is the significance of [concept] in the video?
4. How did the speaker define [term]?
5. What solution was proposed for [problem]?

## Contributors:
- [Abhiraj Adhikary](https://github.com/abhirajadhikary06)
- [Shweta Kumari](https://github.com/ShwetaKumari-programming)

---

Developed with ❤️ by the VidTOMCQ team.
