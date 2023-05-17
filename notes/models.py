from django.db import models
from users.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=256)
    content = models.JSONField(blank=True)
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['updated_at']
    
    def __str__(self) -> str:
        return self.title
    
    