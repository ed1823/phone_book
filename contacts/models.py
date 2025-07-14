from django.db import models
from django.contrib.auth.models import User  # ← для связи с пользователем

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Кто добавил
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    # !!ADD
    # created_at: datetime.datetime = (datetime.datetime.now(), null = false)
    # updated_at: datetime.datetime = (null = True)

    def __str__(self):
        return self.name
