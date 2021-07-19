from django import forms
from django.forms import fields
from .models import *

class TopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea( attrs={'rows': 5,'column':1, 'placeholder': 'What is on your mind?', 'class':'form-control'}), max_length=4000)
    class Meta:
        model = Topic
        fields = ('subject','message')
    def __init__(self, *args, **kwargs):
            super(TopicForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
            self.fields['subject'].widget.attrs['class'] = 'form-control'
            self.fields['subject'].widget.attrs['placeholder'] = 'Subject'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_message', )
 