import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import RobustScaler
import sklearn

# Load the pre-trained model
model = joblib.load(r'C:\Users\Rohan\rohan ML\all projects\github\-data_science_end_to_end_projects\model\model.joblib')  # or use pickle.load(open('model.pkl', 'rb'))

# Load the pre-trained RobustScaler (if it was saved during training)
robust_scaler = joblib.load(r'C:\Users\Rohan\rohan ML\all projects\github\-data_science_end_to_end_projects\model\robust_scaler.joblib')  # or use pickle.load(open('robust_scaler.pkl', 'rb'))

# Reverse mappings
reverse_Order_Priority = {'Not Specified': 0, 'High': 1, 'Low': 2, 'Critical': 3, 'Medium': 4}
reverse_Ship_Mode = {'Regular Air': 0, 'Express Air': 1}
reverse_Region = {'West': 0, 'Atlantic': 1, 'Northwest Territories': 2, 'Prarie': 3, 'Ontario': 4, 'Nunavut': 5}
reverse_Customer_Segment = {'Corporate': 0, 'Consumer': 1, 'Home Office': 2, 'Small Business': 3}
reverse_Product_Category = {'Office Supplies': 0, 'Technology': 1, 'Furniture': 2}
reverse_Product_Container = {'Small Box': 0, 'Large Box': 1, 'Medium Box': 2}

# Streamlit app
st.title('Order Prediction App')

# Input form
Order_Priority = st.selectbox('Order Priority', list(reverse_Order_Priority.keys()))
Order_Quantity = st.number_input('Order Quantity', min_value=1)
Sales = st.number_input('Sales', min_value=0.0)
Ship_Mode = st.selectbox('Ship Mode', list(reverse_Ship_Mode.keys()))
Region = st.selectbox('Region', list(reverse_Region.keys()))
Customer_Segment = st.selectbox('Customer Segment', list(reverse_Customer_Segment.keys()))
Product_Category = st.selectbox('Product Category', list(reverse_Product_Category.keys()))
Product_Container = st.selectbox('Product Container', list(reverse_Product_Container.keys()))

# Create a dictionary with the input values
data = {
    'Order_Priority': [Order_Priority],
    'Order_Quantity': [Order_Quantity],
    'Sales': [Sales],
    'Ship_Mode': [Ship_Mode],
    'Region': [Region],
    'Customer_Segment': [Customer_Segment],
    'Product_Category': [Product_Category],
    'Product_Container': [Product_Container]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Map the string labels to numerical codes
df['Order_Priority'] = df['Order_Priority'].map(reverse_Order_Priority)
df['Ship_Mode'] = df['Ship_Mode'].map(reverse_Ship_Mode)
df['Region'] = df['Region'].map(reverse_Region)
df['Customer_Segment'] = df['Customer_Segment'].map(reverse_Customer_Segment)
df['Product_Category'] = df['Product_Category'].map(reverse_Product_Category)
df['Product_Container'] = df['Product_Container'].map(reverse_Product_Container)

# Apply the RobustScaler to the 'Sales' feature
df['Sales'] = robust_scaler.transform(df[['Sales']])

# Make predictions
if st.button('Predict'):
    predictions = model.predict(df)
    formatted_predictions = [round(pred, 2) for pred in predictions]

    # Display the prediction in a larger font
    st.markdown(f"<h1 style='font-size: 36px; color: #4CAF50;'>Predicted Value is {formatted_predictions[0]}</h1>", unsafe_allow_html=True)
