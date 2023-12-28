from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        # BMI calculation
        bmi = calculate_bmi(weight, height)
        bmi_category = interpret_bmi(bmi)

        return render_template('result.html', bmi=bmi, category=bmi_category)

def calculate_bmi(weight, height):
    # BMI calculation formula
    return round((weight / (height ** 2)), 2)

def interpret_bmi(bmi):
    # Interpretation of BMI categories
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal Weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

if __name__ == '__main__':
    app.run(debug=True)
