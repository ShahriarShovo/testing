from django.contrib import admin
from user_auth.models.user import User
from user_auth.models.user_profile import Profile




# Register your models here.


admin.site.register(User)
admin.site.register(Profile)


