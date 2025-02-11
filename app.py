import streamlit as st
import pickle
import pandas as pd

st.title('Predict for Advertising Sale')
st.write('This web app predicts the **Advertising Sale** ')

model= pickle.load(open('model_ad.pkl','rb'))

#get the input from the user 
TV=st.number_input('TV')
Radio=st.number_input('Radio')
Newspaper=st.number_input('Newspaper')


#convert the user input to a dataframe
user_data=pd.DataFrame({'TV':TV,
    'Radio':Radio,
    'Newspaper':Newspaper},index=[0])

#predict the house price
prediction=model.predict(user_data)

if st.button('predict'):
    st.write(f'The prediction is {prediction[0]*100000}')