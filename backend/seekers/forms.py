from django import forms
from django.forms import ModelForm
from .models import User, Resume, Rate, Pitch, Comment, RATE_CHOICES

class ResumeForm(ModelForm):

    class Meta:
        model = Resume
        exclude = ('profile', 'date_posted')

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

class PitchForm(ModelForm):

    class Meta:
        model = Pitch
        exclude = ('profile', 'date_posted')

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        exclude = ('profile', 'date_posted', 'pitch')

