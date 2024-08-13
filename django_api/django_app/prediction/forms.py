from django import forms

class PredictForm(forms.Form):
    order_priority = forms.ChoiceField(choices=[('Not Specified', 'Not Specified'), ('High', 'High'), ('Low', 'Low'), ('Critical', 'Critical'), ('Medium', 'Medium')])
    order_quantity = forms.IntegerField(min_value=1)
    sales = forms.FloatField(min_value=0.0)
    ship_mode = forms.ChoiceField(choices=[('Regular Air', 'Regular Air'), ('Express Air', 'Express Air')])
    region = forms.ChoiceField(choices=[('West', 'West'), ('Atlantic', 'Atlantic'), ('Northwest Territories', 'Northwest Territories'), ('Prarie', 'Prarie'), ('Ontario', 'Ontario'), ('Nunavut', 'Nunavut')])
    customer_segment = forms.ChoiceField(choices=[('Corporate', 'Corporate'), ('Consumer', 'Consumer'), ('Home Office', 'Home Office'), ('Small Business', 'Small Business')])
    product_category = forms.ChoiceField(choices=[('Office Supplies', 'Office Supplies'), ('Technology', 'Technology'), ('Furniture', 'Furniture')])
    product_container = forms.ChoiceField(choices=[('Small Box', 'Small Box'), ('Large Box', 'Large Box'), ('Medium Box', 'Medium Box')])