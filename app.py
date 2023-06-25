from flask import Flask, render_template,  request
import pickle


app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/predict', methods=['GET', 'Post'])
def predict():
    
    predicted = model.predict([[float(request.form.get('hour'))]])
    output = round(predicted[0],2)
    print(output)
    return render_template('index.html', prediction_text= f"You can score: {output} ")

if __name__ == '__main__':
    app.run(debug=True)