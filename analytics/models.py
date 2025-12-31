from django.db import models

# Create your models here.


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    date = models.DateField(auto_now_add=True)
    first_seen = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('ip_address', 'user_agent', 'date')

    def __str__(self):
        return f"{self.ip_address} | {self.date}"