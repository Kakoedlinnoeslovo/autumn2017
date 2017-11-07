from django import forms
from music.models import Track


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('title', 'duration', 'release_date')
