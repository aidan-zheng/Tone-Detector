from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from google import genai
import os
import json

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        text = data.get('text')
        recipient = data.get('recipient')
        goal = data.get('goal')

        prompt = f"""
        You are a helpful assistant that analyzes the tone and intent of messages. You are an expert in workplace communication and emotional intelligence.

        Analyze the tone of this message and respond only in JSON with:
        - overallTone: one word describing the overall tone
        - score: a number from 0 to 10 where 0 is extremely hostile/unfriendly and 10 is extremely warm/friendly.
        - flaggedPhrases: array of objects with "phrase" and "reason" but make the reason concise (1-3 words)
        - suggestions: array of objects with "original" and "rewrite"
        - summary: a two sentenced summary IN ENGLISH of how this rewrite will land
        - rewrite: a rewritten version of the message that is more effective and appropriate for the recipient and goal. Follow the suggestions proposed in the suggestions array.

        Recipient: {recipient}
        Goal: {goal}
    
        Message: 
        {text}

        Respond ONLY in JSON , no markdown, no backticks, no extra text. Only the 2 senteced summary should be in ENGLISH
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        raw = response.text.strip()
        print("RAW RESPONSE:", raw)

        # Clean response and parse JSON
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()
    
        result = json.loads(raw)
        return jsonify(result)
    
    except Exception as e:
        print("Error: ", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
