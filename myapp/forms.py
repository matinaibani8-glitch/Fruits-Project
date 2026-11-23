from django import forms
from .models import userdata

class userform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = "__all__"

        
class updateform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = ["firstname","lastname","email","password","city","state","num"]