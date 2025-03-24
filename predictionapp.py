import streamlit as st
import sklearn
import pickle as pk
import pandas as pd
from sklearn.preprocessing import StandardScaler

#Load the model
with open('telecom.pickle','rb') as model_file:
    model=pk.load(model_file)

#Load the standardscaler
with open('scaler.pickle','rb') as scaler_file:
    scaler=pk.load(scaler_file)

st.title("Customer Churn Prediction")
st.image('https://www.touchpoint.com/wp-content/uploads/2023/02/5.-Customer-churn-article.png',width=500)

#Taking input from user
st.header('Enter all values to predict if customer will churn or not.')
tenure=st.number_input('Tenure ',min_value=0)

monthly_charges=st.number_input('Monthly charges ',min_value=0.00,step=0.01)

contract_type_mapping = {
    "Month-to-month": 0.0,  
    "One year": 1.0,  
    "Two year": 2.0
}
selected_contract=st.selectbox('Select contract type',list(contract_type_mapping.keys()))
contract_type=contract_type_mapping[selected_contract]

customer_support_calls=st.number_input('Customer support calls ',min_value=0)

internet_service_mapping={
    'Fiber optic':1.0,    
    'DSL': 0.0,            
    'No': 2.0
}
selected_internet_service=st.selectbox('Select internet service',list(internet_service_mapping.keys()))
internet_service=internet_service_mapping[selected_internet_service]

online_security_mapping={
    'No':0.0,
    'Yes':1.0
}
selected_online_security=st.selectbox('Does it have online security? ',list(online_security_mapping.keys()))
online_security=online_security_mapping[selected_online_security]

tech_support_mapping={
    'No':0.0,
    'Yes':1.0
}
selected_tech_support=st.selectbox('Does it have tech support? ',list(tech_support_mapping.keys()))
tech_support=tech_support_mapping[selected_tech_support]

payment_method_mapping={
    'Bank transfer':0.0,
    'Mailed check':3.0,
    'Credit card':1.0,
    'Electronic check':2.0
}
selected_payment_method=st.selectbox('What is the payment method? ',list(payment_method_mapping.keys()))
payment_method=payment_method_mapping[selected_payment_method]

paperless_billing_mapping={
    'Yes':1.0,
    'No':0.0
}
selected_paperless_billing=st.selectbox('Is it paperless billing? ',list(paperless_billing_mapping.keys()))
paperless_billing=paperless_billing_mapping[selected_paperless_billing]

df=pd.DataFrame([[tenure,monthly_charges,contract_type,customer_support_calls,internet_service,online_security,tech_support,payment_method,paperless_billing]],columns=['tenure','monthly_charges','contract_type','customer_support_calls','internet_service','online_security','tech_support','payment_method','paperless_billing'])

#Apply standardscaler before prediction
df_scaled=scaler.transform(df) 

#For prediction
if st.button('Predict'):
    st.success('The data is submitted.')
    result=model.predict(df_scaled)

    if int(result[0])==1:
        st.error("The customer is likely to churn.")
    else:
        st.success('The customer is likely to stay.')

st.write('## Key Factors Affecting Churn: ')
st.write('🌟Long Tenure – Customers who have stayed longer tend to stay.')
st.write('🌟Lower Monthly Charges – High charges often lead to churn.')
st.write('🌟Two-Year Contract – Long-term contracts reduce churn.')
st.write('🌟Fewer Customer Support Calls – More complaints indicate dissatisfaction.')
st.write('🌟DSL Internet – Fiber optic customers may churn more due to cost.')
st.write('🌟Online Security & Tech Support Enabled – These services increase retention.')
st.write('🌟Credit Card or Bank Transfer Payment – Electronic check payments tend to correlate with churn.')
st.write('🌟Paperless Billing Disabled – Some customers prefer traditional billing.')