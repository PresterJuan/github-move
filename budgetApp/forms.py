from django import forms
from budgetApp.models import Stuff

class NewCategory(forms.ModelForm):
    class Meta():
        model = Stuff
        fields = "__all__"
