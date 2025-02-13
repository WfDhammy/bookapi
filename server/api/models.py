import uuid
from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    image = models.ImageField(upload_to='Author')
    othername = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField()
    phone_number_1 = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name



class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


