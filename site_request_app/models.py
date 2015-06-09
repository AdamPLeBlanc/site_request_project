from django.db import models

class Request(models.Model):
    title = models.CharField(max_length=20)
    create_date = models.DateTimeField('date created')
    description = models.CharField(max_length=2000)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
