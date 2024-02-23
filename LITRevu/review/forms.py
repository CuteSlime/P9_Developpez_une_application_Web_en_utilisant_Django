from django import forms

from .models import Review, UserFollows
from accounts.models import CustomUser


class RatingForm(forms.ModelForm):
    """
    A form for creating a Review. It includes fields for the headline,
    body, and rating of the review.
    The rating field is validated to ensure it is an integer between 0 and 5.
    """

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
        labels = {
            "headline": "Titre de votre critique",
            "body": "Votre critique",
            "rating": "note",
        }

    def clean_rating(self):
        data = self.cleaned_data['rating']
        if data not in [str(i) for i in range(6)]:
            raise forms.ValidationError(
                "Invalid rating! Rating must be between 0 and 5.")
        return int(data)


class FollowUserForm(forms.Form):
    """
    A form for following a user. It includes a field for the username of the user to follow.
    The username field is validated to ensure that:
    - the user exists
    - the user is not already followed by the current user
    - the user is not the current user themselves.
    """

    username = forms.CharField(max_length=150)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user_to_follow = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("Cette utilisateur n'existe pas.")
        if UserFollows.objects.filter(user=self.user, followed_user=user_to_follow).exists():
            raise forms.ValidationError("Vous suivez déjà cette utilisateur.")
        if user_to_follow == self.user:
            raise forms.ValidationError(
                "Vous ne pouvez pas vous abonner à vous même.")
        return username
