from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI

app = Flask(__name__)

# sample route
@app.route('/', methods=["GET", "POST"])
def home():

    response = ""
    if request.method == "POST":
        user_input = request.form['user_input']
        # insert key below from email
        client = OpenAI(api_key="")


        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
    )

        response = completion.choices[0].message.content
        
    return render_template('index.html', title='My First Flask App', response = response)

if __name__ == "__main__":

    app.run(debug=True)