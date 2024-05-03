from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Import UserAdmin class

# Register User model with UserAdmin class (pre-configured for user management)
admin.site.register(UserAdmin)
