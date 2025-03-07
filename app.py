#import streamlit as st

# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# url = 'https://taxifare-306051821410.europe-west1.run.app/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

import streamlit as st
import requests
import datetime
import pandas as pd

# Titre de l'application
st.title("🚖 Taxi Fare Prediction")

# ✅ 1️⃣ Formulaire pour entrer les données
st.subheader("📍 Enter your ride details")

pickup_datetime = st.text_input("Date & Time (YYYY-MM-DD HH:MM:SS)", str(datetime.datetime.now()))
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.981267)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.752728)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)

# ✅ 2️⃣ Affichage de la carte interactive
st.subheader("🗺 Ride Map")
map_data = pd.DataFrame({
    "lat": [pickup_latitude, dropoff_latitude],
    "lon": [pickup_longitude, dropoff_longitude]
})
st.map(map_data)

# ✅ 3️⃣ Bouton pour appeler l'API
if st.button("🔮 Predict Fare"):
    # ✅ 4️⃣ Préparation des données pour l'API
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # ✅ 5️⃣ Envoi de la requête à l'API
    url = "https://taxifare-306051821410.europe-west1.run.app/predict"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Vérifie si la requête a réussi
        data = response.json()

        # ✅ 6️⃣ Affichage du résultat
        st.success(f"💰 Estimated Fare: ${data['fare']:.2f}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ API Error: {e}")
