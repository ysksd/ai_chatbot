from flask import Flask, render_template, request
from openai import OpenAI
import config

app = Flask(__name__)

# APIキーの設定
client = OpenAI(api_key=config.OPENAI_API_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["user_input"]

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            response_text = response.choices[0].message.content
        except Exception as e:
            response_text = f"エラーが発生しました: {str(e)}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
