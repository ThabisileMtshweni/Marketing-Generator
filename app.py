from flask import Flask, render_template, request
import cohere
import json
import time
import os

# Initialize Flask app
app = Flask(__name__)

# Load Cohere API key
COHERE_API_KEY = "YXTGgrimFknlWU4RDwfKjHYKuH2DD0pUnT6bu9EY"  # Replace this with your real Cohere API key
co = cohere.Client(COHERE_API_KEY)

# Load prompt templates
with open("prompts.json") as f:
    prompt_templates = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        start_time = time.time()

        prompt_type = request.form.get("prompt_type")
        tone = request.form.get("tone")
        product = request.form.get("product")
        audience = request.form.get("audience")
        extra = request.form.get("extra")

        # Choose prompt template
        prompt_template = prompt_templates.get(prompt_type, "")
        prompt = prompt_template.format(
            tone=tone, product=product, audience=audience, extra=extra
        )

        try:
            response = co.generate(
                model="command",  # or "command-light" if you want a smaller model
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            result = response.generations[0].text.strip()
        except Exception as e:
            result = f"Error: {str(e)}"

        end_time = time.time()
        elapsed = round(end_time - start_time, 2)

        return render_template("index.html", result=result, time=elapsed)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
