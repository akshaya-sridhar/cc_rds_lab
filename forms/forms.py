from django import forms
from .models import covid_19

class CovidForm(forms.ModelForm):
    class Meta:
        model = covid_19
        fields = "__all__"
        widgets = {
            'State_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Date_of_Record': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'No_of_Samples': forms.NumberInput(attrs={'class': 'form-control'}),
            'No_of_Deaths': forms.NumberInput(attrs={'class': 'form-control'}),
            'No_of_Positive': forms.NumberInput(attrs={'class': 'form-control'}),
            'No_of_Negative': forms.NumberInput(attrs={'class': 'form-control'}),
            'No_of_Discharge': forms.NumberInput(attrs={'class': 'form-control'}),
        }