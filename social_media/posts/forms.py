from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control col-md-6'
            })
        }
