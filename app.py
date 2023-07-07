import pickle
import streamlit as st
import sklearn


model = pickle.load(open('car_price_model.sav', 'rb'))

st.title('Toyota - Car Price Prediction')
st.markdown("[UK usedcar dataset](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes)")

year = st.number_input('Input car product year (between 1990 - 2020)',1998,2020,2000)
mileage = st.number_input('Input car mileage(distance used)')
tax = st.number_input('Input car tax(road tax)')
mpg = st.number_input('Input car mpg(miles per gallon)')
engine_size = st.number_input('Input car engine size',1.0,2.5,1.5)

prediction = ' '

if st.button('Predict'):
    prediction = model.predict([[year, mileage, tax, mpg, engine_size]])
    st.write('The price of the car is EUR ',prediction)
    st.write('The price of the car is IDR ',prediction*16400)
