from django import forms
from todoapp.models import Todo

class Newtask(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
                'title':forms.TextInput(attrs = {'class' : 'form-control'}),
                'description':forms.TextInput(attrs = {'class' : 'form-control'})
                

        }
