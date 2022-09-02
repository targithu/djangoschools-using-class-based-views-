from django import forms

class ContactForm(forms.Form):
    name=forms.CharField()
    message=forms.CharField(widget=forms.Textarea)
    widgets={
        'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the name of the respective teacher'}),
        'message':forms.Textarea(attrs={'class':'form-control'}),
    }