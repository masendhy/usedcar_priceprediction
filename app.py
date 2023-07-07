import pickle
import streamlit as st
import sklearn


model = pickle.load(open('car_price_model.sav', 'rb'))

st.title('Car Price Prediction')

year = st.number_input('Input car product year')
mileage = st.number_input('Input car mileage')
tax = st.number_input('Input car tax')
mpg = st.number_input('Input car mpg')
engine_size = st.number_input('Input car engine size')

prediction = ' '

if st.button('Predict'):
    prediction = model.predict([[year, mileage, tax, mpg, engine_size]])
    st.write('The price of the car is EUR ',prediction)
    st.write('The price of the car is IDR ',prediction*16400)
