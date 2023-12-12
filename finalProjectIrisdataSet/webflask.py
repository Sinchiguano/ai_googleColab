#import flask
from flask import Flask
from flask import render_template
from flask import request
import pickle
import numpy as np


myapp=Flask(__name__)



sepal_length_new=[]
sepal_width_new=[]
petal_length_new=[]
petal_width_new=[]
species_new=[]


@myapp.route('/')
def index():
    #print("Sinchiguano Cesar")
    #return 'WEB APP WITH PYTHON FLASK'
    return render_template('index.html')




@myapp.route('/simple_predict',methods=['POST','GET'])
def simple_predict():

    sepal_length=request.form["SepalLength"]
    sepal_width=request.form["SepalWidth"]
    petal_length=request.form["PetalLength"]
    petal_width=request.form["PetalWidth"]
    #calling the model
    model=pickle.load(open('finalized_model.pkl', 'rb'))

    print(type(sepal_length))
    print(type(sepal_width))
    print(type(petal_length))

    given_input =np.array([[float(sepal_length),float(sepal_width),float(petal_length),float(petal_width)]])
    # given_input =np.array([[float(petal_length),float(petal_width)]])
    prediction=model.predict(given_input)
    print('The final prediction: '.format(prediction))
    print()
    return render_template("result.html",result=prediction)




if __name__ == '__main__':
    myapp.run(debug=True)


    #https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html
    #https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
    #https://github.com/abishekarjun98/ML_app/blob/main/templates/index.html
