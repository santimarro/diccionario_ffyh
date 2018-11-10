from django import forms
from .models import Word

class NewWord(forms.Form):
	word = forms.CharField(required=True,max_length=30, label="Ingresar palabra")
	meaning = forms.CharField(required=True,max_length=200, label="Ingresar significado")
	example = forms.CharField(max_length=200, label="Ingresar ejemplo de uso")
	origin = forms.CharField(max_length=30, label="Ingresar origen de la palabra")


class ApproveWord(forms.Form):	
	word_id = forms.IntegerField(required=False)
