from django.db import models

class Tables(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField() 
    
    STATUS_CHOICES = (
        ('A', 'Available'),
        ('E', 'Engaged'),
        ('B', 'Booked'),
        ('U', 'Under Maintanance')
    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')

    SEATING_CHOICES =(
        ('AC', "Air Conditioner Room"),
        ('IN', "Indoor Non AC"),
        ('OT', "Outdoor Seating")
    )

    seating = models.CharField(max_length=2, choices=SEATING_CHOICES)

    @classmethod
    def get_available_table(cls, capcity):
        return cls.objects.filter(
            capacity__gte=capcity,
            status='A'
            ).order_by('capacity').first()

    def __str__(self):
        return f"Table: {self.table_number} {self.seating} {self.capacity}"

class Reservations(models.Model):
    customer_name = models.CharField(max_length=200, blank=False)
    phone = models.IntegerField()
    email = models.EmailField()
    no_of_guests = models.IntegerField()
    alloted_table = models.ForeignKey(Tables, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.customer_name} {self.alloted_table}"