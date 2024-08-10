from flask import Flask, request, render_template
import pandas as pd
import joblib 
from sklearn.preprocessing import RobustScaler

app = Flask(__name__)

# Load the pre-trained model and scaler
model = joblib.load(r'C:\Users\Rohan\rohan ML\all projects\github\-data_science_end_to_end_projects\model\model.joblib')
robust_scaler = joblib.load(r'C:\Users\Rohan\rohan ML\all projects\github\-data_science_end_to_end_projects\model\robust_scaler.joblib')

# Reverse mappings
reverse_Order_Priority = {'Not Specified': 0, 'High': 1, 'Low': 2, 'Critical': 3, 'Medium': 4}
reverse_Ship_Mode = {'Regular Air': 0, 'Express Air': 1}
reverse_Region = {'West': 0, 'Atlantic': 1, 'Northwest Territories': 2, 'Prarie': 3, 'Ontario': 4, 'Nunavut': 5}
reverse_Customer_Segment = {'Corporate': 0, 'Consumer': 1, 'Home Office': 2, 'Small Business': 3}
reverse_Product_Category = {'Office Supplies': 0, 'Technology': 1, 'Furniture': 2}
reverse_Product_Container = {'Small Box': 0, 'Large Box': 1, 'Medium Box': 2}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        Order_Priority = request.form['Order_Priority']
        Order_Quantity = int(request.form['Order_Quantity'])
        Sales = float(request.form['Sales'])
        Ship_Mode = request.form['Ship_Mode']
        Region = request.form['Region']
        Customer_Segment = request.form['Customer_Segment']
        Product_Category = request.form['Product_Category']
        Product_Container = request.form['Product_Container']

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
        formatted_predictions = round(predictions[0], 2)

        return render_template('index.html', prediction_text=f'Predicted Value is {formatted_predictions}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
