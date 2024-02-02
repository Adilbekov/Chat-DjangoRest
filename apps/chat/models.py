from django.db import models

from apps.users.models import User
# Create your models here.

    
class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='chat_image'
    )


    def __str__(self):
        return f"Сообщение к {self.to_user} от {self.from_user}"
    
    class Meta:
        verbose_name='Личные сообшение '
        verbose_name_plural='Личные сообшение '

class FrontMessage(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True),
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='chat_image'
    )

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name='Группа: Frontend'
        verbose_name_plural='Группа: Frontend'
    
class BackMessage(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True),
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='chat_image'
    )

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name='Группа: Backend'
        verbose_name_plural='Группа: Backend'
    

class DataScienceMessage(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True),
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='chat_image'
    )

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name='Группа: Data Science'
        verbose_name_plural='Группа: Data Science'