import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from flask import Flask, jsonify

app = Flask(__name__)

# Load mining data
data = pd.read_csv('mining_data.csv')

# Preprocess data
X = data.drop(['target'], axis=1)
y = data['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

@app.route('/api/mining-data', methods=['GET'])
def get_mining_data():
    return jsonify({'data': data.to_dict(orient='records')})

if __name__ == '__main__':
    app.run(debug=True)
