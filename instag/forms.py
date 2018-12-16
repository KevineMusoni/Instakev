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
        # userprofile arguments 
        fields = ('Name','profile_picture','bio' )


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget=forms.TextInput()
        self.fields['text'].widget.attrs['placeholder']='comment...'

    class Meta:
        model = Comment
        fields = ('text',)