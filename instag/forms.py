from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', )

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget=forms.TextInput()
    class Meta:
        model = Profile
        fields = ('Name','profile_picture','bio' )


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget=forms.TextInput()
        self.fields['text'].widget.attrs['placeholder']='Add a comment...'

    class Meta:
        model = Comment
        fields = ('text',)