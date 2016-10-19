from django.db import models


SIGN = [
    ('+','+'),
    ('-','-'),
    ('*','*'),
    ('/','/'),
]

class Operation(models.Model):
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    num1 = models.FloatField()
    num2 = models.FloatField()
    sign = models.CharField(max_length=1, choices=SIGN)

    @property
    def calculate(self):
        sign, num1, num2 = [self.sign, self.num1, self.num2]
        if sign == '+':
            return num1 + num2
        elif sign == '-':
            return num1 - num2
        elif sign == '*':
            return num1 * num2
        else:
            return num1 / num2

USER_TYPE = [
    ('n', 'Normal User'),
    ('o', 'Owner'),
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    user_type = models.CharField(max_length=1, choices=USER_TYPE)

    @property
    def is_owner(self):
        return self.user_type == 'o'
