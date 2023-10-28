from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # A one-to-one relationship is a link between the information in two tables, where each record in each table only appears once. For example, Email - user account. For many websites, one email address is associated with exactly one user account and each user account is identified by its email address, or Country - capital city: Each country has exactly one capital city. Each capital city is the capital of exactly one country.

    # Addition
    portfolioSite = models.URLField(blank=True)
    profilePicture = models.ImageField(upload_to='profilePictures',blank=True)

    def __str__(self):
        return self.user.username
