from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.validators import MinValueValidator

class ItemCategory(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Item Category"
        verbose_name_plural = "Item Categories"

    def __str__(self):
        return self.category_name


class MenuItem(models.Model):
    item_name = models.CharField(
        max_length=200, 
        null=False)
    
    item_description = models.TextField(
        max_length=800, 
        blank=True, 
        null=True)
    
    item_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(0)])
    
    item_category = models.ForeignKey(
        "ItemCategory",  
        on_delete=models.PROTECT,
        related_name="item_category")
    
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)


    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return f"{self.item_name} {self.item_category} {self.item_price}"