from flask import Flask, render_template, request
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Generate a synthetic classification dataset
X, y = make_classification(n_samples=100, n_features=4, random_state=42)




# print(type(X))
# print(X.shape)
# print(X[30:50])



# Train a Random Forest classifier
classifier = RandomForestClassifier()
classifier.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def classification_page():
    if request.method == 'POST':
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        feature3 = float(request.form['feature3'])
        feature4 = float(request.form['feature4'])

        # Create a new sample
        sample = [[feature1, feature2, feature3, feature4]]

        # Make predictions with the classifier
        prediction = classifier.predict(sample)[0]

        return render_template('result.html', feature1=feature1, feature2=feature2, feature3=feature3,
                               feature4=feature4, prediction=prediction)

    return render_template('form.html')

if __name__ == '__main__':
    app.run()
