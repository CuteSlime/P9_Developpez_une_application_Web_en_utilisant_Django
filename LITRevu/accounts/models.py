from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    pass
    # age = models.PositiveIntegerField(null=True, blank=True)
