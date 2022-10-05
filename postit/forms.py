from django import forms

from .models import Postit

MAX_POST_LENGTH = 240


class PostForm(forms.ModelForm):
    class Meta:
        model = Postit
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_POST_LENGTH:
            raise forms.ValidationError("This message is too long")
        return content
