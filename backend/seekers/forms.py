from django import forms
from django.forms import ModelForm
from .models import User, Resume, Rate, Comment, RATE_CHOICES

class UploadResumeForm(forms.ModelForm):
    
    cv = forms.FileField(widget=forms.FileInput(attrs={'class':'file-field input-field col s12', 'placeholder':'Upload your CV'}))
    pitch = forms.CharField(widget=forms.TextInput(attrs={'class':'input-field col s12','placeholder':'submit your elevator pitch'}))
  
    class Meta:
        model = Resume
        fields = ('cv', 'pitch')

class RateForm(forms.ModelForm):
    conciseness = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'browser-default'}),
        choices=RATE_CHOICES, 
        required=True,
    )
    professionalism = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'browser-default'}),
        choices=RATE_CHOICES, 
        required=True,
    )
    flow = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'browser-default'}),
        choices=RATE_CHOICES, 
        required=True,
    )
    class Meta:
        model = Rate
        fields = ('conciseness', 'professionalism', 'flow')

# class PitchForm(ModelForm):

#     class Meta:
#         model = Pitch
#         exclude = ('profile', 'date_posted')

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        exclude = ('profile', 'date_posted', 'pitch')

