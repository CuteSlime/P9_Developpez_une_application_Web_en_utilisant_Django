from django import forms
from .models import Review


class RatingForm(forms.ModelForm):
    RATING_CHOICES = [(i, '') for i in range(6)]
    rating = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.RadioSelect, initial=0)

    class Meta:
        model = Review
        fields = (
            "headline",
            "body",
            "rating",
        )

    def clean_rating(self):
        data = self.cleaned_data['rating']
        if data not in [str(i) for i in range(6)]:
            raise forms.ValidationError(
                "Invalid rating! Rating must be between 0 and 5.")
        return int(data)
