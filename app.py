from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    height_in_meters = height / 100  # convert height from cm to meters
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

def get_weight_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None

    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi(weight, height)
        category = get_weight_category(bmi)

    return render_template('index.html', bmi=bmi, category=category)

@app.route('/weight_categories')
def result():
    # You can include any necessary data processing or logic here
    return render_template('weight_categories.html')

if __name__ == '__main__':
    app.run()