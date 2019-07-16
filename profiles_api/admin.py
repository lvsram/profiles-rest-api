from django.contrib import admin

from profiles_api import models

# this tells django to register our user profile model with admin side so it
# makes it accessible through admin interface
admin.site.register(models.UserProfile)
