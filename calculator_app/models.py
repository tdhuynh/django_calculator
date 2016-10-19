from django.db import models


class Operation(models.Model):
    user = models.ForeignKey('auth.User')
    equation = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user



USER_TYPE = [
    ('n', 'Normal User'),
    ('o', 'Owner'),
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    user_type = models.CharField(max_length=1, choices=USER_TYPE)

    def __str__(self):
        return self.user
