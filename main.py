from flask import Flask, render_template, request, flash, session
from random import sample

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        numbers = "0123456789"
        symbols = "?/\!@#$%&*()_-+={[}]:;,."
        capital_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        small_letter = "abcdefghijklmnopqrstuvwxyz"

        size = int(request.form.get('size'))
        config = ""

        session['numbers'] = request.form.get('numbers')
        session['symbols'] = request.form.get('symbols')
        session['capital_letter'] = request.form.get('capital_letter')
        session['small_letter'] = request.form.get('small_letter')
        session['dark_mode'] = request.form.get('dark_mode')

        if request.form.get('numbers') != None:
            config += numbers
        else:
            numbers = "no"
        
        if request.form.get('symbols') != None:
            config += symbols
        else:
            symbols = "no"

        if request.form.get('capital_letter') != None:
            config += capital_letter
        else:
            capital_letter = "no"

        if request.form.get('small_letter') != None:
            config += small_letter
        else:
            small_letter = "no"

        if numbers == "no" and symbols == "no" and capital_letter == "no" and small_letter == "no":
            flash('At least one option must be checked')
        else:
            password = "".join(sample(config, size))
            print(password)
            return render_template('index.html', variable=password)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'cdsvfvdcx'
    app.run(debug=True, port=5000)