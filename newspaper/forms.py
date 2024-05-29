from django import forms 
from newspaper.models import Comment, Contact, Newsletter

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

# Comment
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"

# Newsletter => Subscribe
class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"