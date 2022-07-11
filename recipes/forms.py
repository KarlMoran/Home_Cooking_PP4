from .models import Comments
from django import forms 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields[
    #         'body'
    #         ].label = ""