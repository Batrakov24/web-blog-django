from django.db import models

# Create your models here.
class feedbackRecord(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    text = models.TextField(blank=False)
    checked = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"Отзыв {self.name} - с id {self.id} ({'Проверен' if self.checked else 'Непроверен'})"
