from django import forms
from django.forms import fields
from .models import *


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
            super(BoardForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['name'].label = "Board Name"
            self.fields['name'].widget.attrs['placeholder'] = 'Board Name'
            self.fields['description'].widget.attrs['class'] = "form-control"
            self.fields['description'].widget.attrs['placeholder'] = "What's in Your mind?" 
            
class TopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea( attrs={'rows': 5,'column':1, 'placeholder': 'What is on your mind?', 'class':'form-control'}), max_length=4000)
    class Meta:
        model = Topic
        fields = ('subject','message')
    def __init__(self, *args, **kwargs):
            super(TopicForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
            self.fields['subject'].widget.attrs['class'] = 'form-control'
            self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
            self.fields['message'].widget.attrs['placeholder'] = "What's in Your mind?"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('message', )

    def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
            self.fields['message'].widget.attrs['class'] = 'form-control'
            self.fields['message'].widget.attrs['placeholder'] = "What's in Your mind?"
