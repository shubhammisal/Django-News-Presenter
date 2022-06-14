from random import choices
from django import forms  
from datetime import date

class newsForm(forms.Form):
    from_date=forms.DateField(widget=forms.DateInput(attrs={'class': 'date','type': 'date','value': date.today()}))

    to_date=forms.DateField(widget=forms.DateInput(attrs={'class': 'date','type': 'date','value':date.today()}))
    