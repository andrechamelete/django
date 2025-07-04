from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None, related_name='category_name')
    # a linha acima seria para FK de uma suposta table Category, related com a coluna 'category_name'
    def __str__(self):
        return self.name + " : " + self.cuisine
    
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter time")

    def __str__(self):
        return self.first_name + " " + self.last_name
    