# import pandas as pd
# import joblib
# from django.shortcuts import render
# from sklearn.preprocessing import RobustScaler
# from .models import Prediction

# # Load the pre-trained model
# model = joblib.load(r'C:\Users\Rohan\rohan ML\all projects\github\-data_science_end_to_end_projects\model\model.joblib')

# # Load the pre-trained RobustScaler (if it was saved during training)
# robust_scaler = joblib.load(r'C:\Users\Rohan\rohan ML\all projects\github\-data_science_end_to_end_projects\model\robust_scaler.joblib')

# # Reverse mappings
# reverse_Order_Priority = {'Not Specified': 0, 'High': 1, 'Low': 2, 'Critical': 3, 'Medium': 4}
# reverse_Ship_Mode = {'Regular Air': 0, 'Express Air': 1}
# reverse_Region = {'West': 0, 'Atlantic': 1, 'Northwest Territories': 2, 'Prarie': 3, 'Ontario': 4, 'Nunavut': 5}
# reverse_Customer_Segment = {'Corporate': 0, 'Consumer': 1, 'Home Office': 2, 'Small Business': 3}
# reverse_Product_Category = {'Office Supplies': 0, 'Technology': 1, 'Furniture': 2}
# reverse_Product_Container = {'Small Box': 0, 'Large Box': 1, 'Medium Box': 2}

# def index(request):
#     if request.method == 'POST':
#         Order_Priority = request.POST['Order_Priority']
#         Order_Quantity = int(request.POST['Order_Quantity'])
#         Sales = float(request.POST['Sales'])
#         Ship_Mode = request.POST['Ship_Mode']
#         Region = request.POST['Region']
#         Customer_Segment = request.POST['Customer_Segment']
#         Product_Category = request.POST['Product_Category']
#         Product_Container = request.POST['Product_Container']

#         # Create a dictionary with the input values
#         data = {
#             'Order_Priority': [Order_Priority],
#             'Order_Quantity': [Order_Quantity],
#             'Sales': [Sales],
#             'Ship_Mode': [Ship_Mode],
#             'Region': [Region],
#             'Customer_Segment': [Customer_Segment],
#             'Product_Category': [Product_Category],
#             'Product_Container': [Product_Container]
#         }

#         # Create the DataFrame
#         df = pd.DataFrame(data)

#         # Map the string labels to numerical codes
#         df['Order_Priority'] = df['Order_Priority'].map(reverse_Order_Priority)
#         df['Ship_Mode'] = df['Ship_Mode'].map(reverse_Ship_Mode)
#         df['Region'] = df['Region'].map(reverse_Region)
#         df['Customer_Segment'] = df['Customer_Segment'].map(reverse_Customer_Segment)
#         df['Product_Category'] = df['Product_Category'].map(reverse_Product_Category)
#         df['Product_Container'] = df['Product_Container'].map(reverse_Product_Container)

#         # Apply the RobustScaler to the 'Sales' feature
#         df['Sales'] = robust_scaler.transform(df[['Sales']])

#         # Make predictions
#         predictions = model.predict(df)
#         formatted_predictions = [round(pred, 2) for pred in predictions]

#         # Save the data to the database
#         prediction_instance = Prediction(
#             order_priority=Order_Priority,
#             order_quantity=Order_Quantity,
#             sales=Sales,
#             ship_mode=Ship_Mode,
#             region=Region,
#             customer_segment=Customer_Segment,
#             product_category=Product_Category,
#             product_container=Product_Container,
#             prediction=formatted_predictions[0]
#         )
#         prediction_instance.save()

#         return render(request, 'prediction/result.html', {'prediction': formatted_predictions[0]})

#     return render(request, 'prediction/index.html')

# prediction/views.py   


import pandas as pd
import joblib
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Prediction
from .serializers import PredictionSerializer
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


from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        data = request.data

        Order_Priority = data.get('Order_Priority')
        Order_Quantity = data.get('Order_Quantity')
        Sales = data.get('Sales')
        Ship_Mode = data.get('Ship_Mode')
        Region = data.get('Region')
        Customer_Segment = data.get('Customer_Segment')
        Product_Category = data.get('Product_Category')
        Product_Container = data.get('Product_Container')

        if not all([Order_Priority, Order_Quantity, Sales, Ship_Mode, Region, Customer_Segment, Product_Category, Product_Container]):
            return Response({"error": "Missing input data"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a dictionary with the input values
        input_data = {
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
        df = pd.DataFrame(input_data)

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

        # Save the data to the database
        prediction_instance = Prediction(
            order_priority=Order_Priority,
            order_quantity=Order_Quantity,
            sales=Sales,
            ship_mode=Ship_Mode,
            region=Region,
            customer_segment=Customer_Segment,
            product_category=Product_Category,
            product_container=Product_Container,
            prediction=formatted_predictions[0]
        )
        prediction_instance.save()

        return Response({'prediction': formatted_predictions[0]}, status=status.HTTP_200_OK)

@api_view(['GET'])
def prediction_list(request):
    predictions = Prediction.objects.all()
    serializer = PredictionSerializer(predictions, many=True)
    return Response(serializer.data)
