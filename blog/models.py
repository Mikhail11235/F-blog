from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200) 
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        )
    body = models.TextField()


    def bodyFirst100(self):
        if len(self.body) >= 100:
            return self.body[:100] + '...'
        return self.body
    
    
    def __str__(self):
        return self.title
