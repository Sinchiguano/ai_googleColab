from flask import Flask, render_template, request
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

app = Flask(__name__)

# # load the model from disk
# import pickle
# classifier=pickle.load(open('finalized_model.pkl', 'rb'))


# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a Random Forest classifier
classifier = RandomForestClassifier()
classifier.fit(X, y)


@app.route('/', methods=['GET', 'POST'])
def iris_classifier():
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        
        # Create a new Iris sample
        sample = np.array([[float(sepal_length),float(sepal_width),float(petal_length),float(petal_width)]])
        
        # Make predictions with the classifier
        prediction = classifier.predict(sample)[0]
        
        # Map the predicted label to the corresponding flower species
        species = iris.target_names[prediction]
        
        return render_template('result.html', sepal_length=sepal_length, sepal_width=sepal_width,
                               petal_length=petal_length, petal_width=petal_width, species=species)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
