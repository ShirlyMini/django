from django import forms

class Studentregister(forms.Form):
    name = forms.CharField(max_length=20)
    marks= forms.IntegerField()
    address = forms.CharField(max_length=200)
