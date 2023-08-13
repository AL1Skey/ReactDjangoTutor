from django.db import models
import random
import string #for ASCII

def generate_code():
    length=7
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase(),k=length))
        if Room.objects.filter(code=code).count == 0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8,default="",unique=True)
    host = models.CharField(max_length=8,unique=True)
    can_pause = models.BooleanField(null=False, default=False)
    skip_vote = models.IntegerField(null=False, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    