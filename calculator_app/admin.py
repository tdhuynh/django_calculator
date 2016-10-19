from django.contrib import admin
from calculator_app.models import Operation, Profile

admin.site.register([Operation, Profile])
