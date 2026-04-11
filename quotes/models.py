from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    character = models.CharField(max_length=100)
    source = models.CharField(max_length=200, help_text="Episode or Movie")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'"{self.character}: {self.quote[:50]}..."'
