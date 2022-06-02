from django import forms
from .models import Posts
class PostCreate(forms.ModelForm):
    class Meta:
        model=Posts
        fields='__all__'
        # fields=()
        # exclude=('')
