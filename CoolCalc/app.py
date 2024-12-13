from flask import Flask, render_template, request
import answerchecker as ac
import memorybank as mb
import rando_num as rn

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer_checker', methods=['POST'])
def answer_checker():
    # Assume your answer_checker function returns a string with the result
    result = ac.answer_checker()
    return result

@app.route('/memorybank', methods=['GET', 'POST']) 
def memory_bank(): 
    lines = mb.read_file() 
    if request.method == 'POST': 
        user_answers = request.form.getlist('answers') 
        correct_answers = [line[1] for line in lines] 
        results = [user == correct for user, correct in zip(user_answers, correct_answers)] 
        return render_template('memorybank.html', equations=lines, results=results) 
    return render_template('memorybank.html', equations=lines)

@app.route('/number_guesser', methods=['POST'])
def number_guesser():
    result = rn.random_number()
    return result

if __name__ == '__main__':
    app.run(debug=True)
