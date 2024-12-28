from django import forms

class CalculateForm(forms.Form):
    a = forms.IntegerField(label="Первое число: ", max_value=100, min_value=0)
    b = forms.IntegerField(label="Второе число: ", max_value=100, min_value=0)
