from django.db import models

class Prediction(models.Model):
    order_priority = models.CharField(max_length=50)
    order_quantity = models.IntegerField()
    sales = models.FloatField()
    ship_mode = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    customer_segment = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    product_container = models.CharField(max_length=50)
    prediction = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id} - {self.timestamp}"
