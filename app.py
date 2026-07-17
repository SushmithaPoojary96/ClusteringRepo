from flask import Flask, render_template, request
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

app = Flask(__name__)

data = {
    "age" : [20, 22, 25, 30, 35, 40, 45, 50, 23, 37],
    "spending" : [30, 35, 40, 60, 65, 70, 80, 85, 85, 38]
}

df = pd.DataFrame(data)

X = df[['age', 'spending']]

model = KMeans(n_clusters=2, random_state=42)
model.fit(X)

centers = model.cluster_centers_

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    spending = float(request.form['spending'])

    new_point = np.array([[age, spending]])

    # Find nearest cluster
    distances = np.linalg.norm(centers - new_point, axis=1)
    cluster = np.argmin(distances)

    return render_template('index.html', prediction=int(cluster))
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)