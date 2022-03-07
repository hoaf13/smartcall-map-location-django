from django.db import models

# Create your models here.
class Report(models.Model):
    conversation_id = models.CharField(max_length=50, null=True)
    address_value = models.CharField(max_length=256,  null=True) 
    address_text = models.CharField(max_length=256,  null=True)
    location = models.JSONField(null=True) 
    customer_phone = models.CharField(max_length=16, null=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.conversation_id} - {self.address_text}"