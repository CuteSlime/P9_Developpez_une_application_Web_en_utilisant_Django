from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import CustomUser


class Ticket(models.Model):
    """
    A model representing a Ticket.

    Attributes:
        title (CharField): The title of the ticket.
        description (TextField): The description of the ticket.
        user (ForeignKey): The user who created the ticket.
        image (ImageField): The image associated with the ticket.
        time_created (DateTimeField): The time the ticket was created.
    """

    # Your Ticket model definition goes here
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    """
    A model representing a Review.

    Attributes:
        ticket (ForeignKey): The ticket that the review is for.
        rating (PositiveSmallIntegerField): The rating given in the review.
        headline (CharField): The headline of the review.
        body (TextField): The body text of the review.
        user (ForeignKey): The user who created the review.
        time_created (DateTimeField): The time the review was created.
    """

    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.headline}'


class UserFollows(models.Model):
    """
    A model representing a UserFollows relationship.

    Attributes:
        user (ForeignKey): The user who is following.
        followed_user (ForeignKey): The user who is being followed.
    """

    # Your UserFollows model definition goes here
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)
    followed_user = models.ForeignKey(CustomUser,
                                      on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )

    def __str__(self):
        return f'{self.user.username} suit {self.followed_user.username}'
