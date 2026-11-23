# Tone Detector

A Flask web app that analyzes the tone of an email before you send it. Paste in a draft and Tone Detector scores the tone, flags the phrases that cause problems, and suggests rewrites.

<!-- Add a screenshot here, e.g. ![Tone Detector screenshot](static/screenshot.png) -->

## Features

- **Tone scoring:** Gives your email an overall tone score.
- **Flagged phrases:** Highlights the specific phrases that affect the score, so the score is explained rather than just a number.
- **Suggested rewrites:** Offers alternative wording for problematic phrases.
- **Two-screen flow:** Paste your email on the first screen and view results on the second.
- **Loading screen with progress bar:** Shows progress while the analysis runs and handles error states.

## How It Works

1. You paste an email into the app.
2. The Flask backend sends the text to the Gemini API (`gemini-2.5-flash`) with a prompt that asks for a tone score, flagged phrases, and rewrites.
3. The backend returns the result and the frontend displays it.

Gemini sometimes misjudged tone in early versions. I improved accuracy by refining the prompt so that the tone score is always paired with flagged phrases that explain it.

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini API (`gemini-2.5-flash`)
- **Frontend:** HTML, CSS, JavaScript

## Getting Started

### Prerequisites

- Python 3.9 or newer
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### Installation

```bash
# Clone the repository
git clone https://github.com/aidan-zheng/Tone-Detector.git
cd Tone-Detector

# Create and activate a virtual environment
python -m venv tone-detect
source tone-detect/bin/activate        # On Windows: tone-detect\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root and add your API key:

```
GEMINI_API_KEY=your_api_key_here
```

Never commit your `.env` file. It is listed in `.gitignore`.

### Run the App

```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Project Structure

```
Tone-Detector/
├── app.py            # Flask routes and Gemini API integration
├── templates/
│   └── index.html    # Frontend pages
├── static/           # CSS and JavaScript
├── requirements.txt
└── .env              # Your API key (not committed)
```
