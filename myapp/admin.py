from django.contrib import admin
from myapp.models import Role, UserRole

admin.site.register(Role)
admin.site.register(UserRole)
