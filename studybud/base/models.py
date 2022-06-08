from django.db import models

'''
Username (leave blank to use 'seansmith'): 
Email address: sean@sean.com
Password: 
Password (again):
←[31;1mThis password is too common.
←[0mBypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
'''

# Create your models here.
class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


