from django.db import models

class CustomerProfile(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.TextField(blank=True)


    def __str__(self):
        return f"Customer: {self.name}"