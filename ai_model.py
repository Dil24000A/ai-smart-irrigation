import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import firebase_admin
from firebase_admin import credentials, db
import time

# Firebase setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://YOUR_PROJECT.firebaseio.com/'
})

ref = db.reference('/')

# Load dataset
data = pd.read_csv("../dataset/data.csv")

X = data[['moisture', 'temperature', 'humidity']]
y = data['water_needed']

# Better model
model = RandomForestClassifier()
model.fit(X, y)

while True:
    moisture = ref.child("moisture").get()
    temperature = 30
    humidity = 60

    prediction = model.predict([[moisture, temperature, humidity]])

    if prediction[0] == 1:
        ref.update({"pump": "ON"})
    else:
        ref.update({"pump": "OFF"})

    time.sleep(5)