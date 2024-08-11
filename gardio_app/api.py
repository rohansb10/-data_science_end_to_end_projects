from gradio_client import Client

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		Order_Priority="Not Specified",
		Order_Quantity=3,
		Sales=3,
		Ship_Mode="Regular Air",
		Region="West",
		Customer_Segment="Corporate",
		Product_Category="Office Supplies",
		Product_Container="Small Box",
		api_name="/predict"
)
print(result)