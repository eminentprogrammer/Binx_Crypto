import uuid
from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


class Transfer(models.Model):
    id                  = models.UUIDField(primary_key=True, unique=True, blank=True)
    sender              = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="sender")
    recipient_name      = models.CharField(max_length=200)
    recipient_account   = models.CharField(max_length=20)
    recipient_bank      = models.CharField(max_length=5)
    amount              = models.FloatField(default=0)
    status              = models.CharField(max_length=100, choices=(("pending", "Pending"), ("success", "Success"), ("failed", "Failed")), default="pending")
    created_at          = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    
    def save(self, *args, **Kwargs):
        if not self.id:
            self.id = str(uuid.uuid4()).replace('-', '')
            
        return super(Transfer, self).save(*args, **Kwargs)