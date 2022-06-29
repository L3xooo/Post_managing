from django import forms
from django.forms import ModelForm
from django import forms
from .models import Post
import requests

class PostEdit(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['id','userId']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
    def clean(self):
        cleaned_data = super().clean()
        userId = str(cleaned_data.get('userId'))
        Id = cleaned_data.get('id')
        url = f'https://jsonplaceholder.typicode.com/users/{userId}'
        response = requests.get(url)
        data = response.json()
        if bool(data) == False:
            raise forms.ValidationError("This userId does not exist!")
        if Id <= 0:
            raise forms.ValidationError("Post Id must be grater than 0!")
        
