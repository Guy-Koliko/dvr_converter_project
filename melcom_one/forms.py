from django import forms

class FilterForm(forms.Form):
    date = forms.CharField(max_length=100)
    starttime = forms.CharField(max_length=10)
    endtime = forms.CharField(max_length=10)
   