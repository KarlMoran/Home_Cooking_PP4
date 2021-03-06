from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comments, Post

class ContactForm(forms.Form):
    """ 
    Contact form
    """
    first_name = forms.CharField(label='Your name', max_length=100)
    last_name = forms.CharField(label='Your Last name', max_length=50)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
    email_address = forms.EmailField(label='Your Email', max_length=150)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields[
            'body'
            ].label = ""

class RecipeForm(forms.ModelForm):
    """
    Recipe Form 
    """
    class Meta:
        """ 
        fields for recipe form
        """
        model = Post
        fields = ('title', 'description', 'ingredients',
                  'preparation_steps', 'image')

        widgets = {
            'ingredients': SummernoteWidget(),
            'preparation_steps': SummernoteWidget(),
            'description': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields[
            'image'
            ].label = "You can upload an image here"