from django import forms
from .models import Word

class PostForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ('word_text',)