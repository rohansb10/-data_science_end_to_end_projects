import gradio as gr
import pandas as pd
import joblib
from sklearn.preprocessing import RobustScaler

# Load the pre-trained model
model = joblib.load(r'C:\Users\Rohan\rohan ML\all projects\github\-data_science_end_to_end_projects\model\model.joblib')

# Load the pre-trained RobustScaler (if it was saved during training)
robust_scaler = joblib.load(r'C:\Users\Rohan\rohan ML\all projects\github\-data_science_end_to_end_projects\model\robust_scaler.joblib')

# Reverse mappings
reverse_Order_Priority = {'Not Specified': 0, 'High': 1, 'Low': 2, 'Critical': 3, 'Medium': 4}
reverse_Ship_Mode = {'Regular Air': 0, 'Express Air': 1}
reverse_Region = {'West': 0, 'Atlantic': 1, 'Northwest Territories': 2, 'Prarie': 3, 'Ontario': 4, 'Nunavut': 5}
reverse_Customer_Segment = {'Corporate': 0, 'Consumer': 1, 'Home Office': 2, 'Small Business': 3}
reverse_Product_Category = {'Office Supplies': 0, 'Technology': 1, 'Furniture': 2}
reverse_Product_Container = {'Small Box': 0, 'Large Box': 1, 'Medium Box': 2}

def predict(Order_Priority, Order_Quantity, Sales, Ship_Mode, Region, Customer_Segment, Product_Category, Product_Container):
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
    predictions = model.predict(df)
    formatted_predictions = [round(pred, 2) for pred in predictions]

    return f"Predicted Value is {formatted_predictions[0]}"

# Define the Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(list(reverse_Order_Priority.keys()), label="Order Priority"),
        gr.Number(label="Order Quantity", minimum=1),
        gr.Number(label="Sales", minimum=0.0),
        gr.Dropdown(list(reverse_Ship_Mode.keys()), label="Ship Mode"),
        gr.Dropdown(list(reverse_Region.keys()), label="Region"),
        gr.Dropdown(list(reverse_Customer_Segment.keys()), label="Customer Segment"),
        gr.Dropdown(list(reverse_Product_Category.keys()), label="Product Category"),
        gr.Dropdown(list(reverse_Product_Container.keys()), label="Product Container")
    ],
    outputs="text",
    title="Order Prediction App",
    description="Enter the details to predict the order value."
)

# Launch the Gradio app
iface.launch()
