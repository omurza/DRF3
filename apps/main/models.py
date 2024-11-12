from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=220,verbose_name='заголовк')
    description=models.TextField(verbose_name='описание')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='дата создания')
    pages=models.IntegerField(max_length=600,verbose_name="колво-страниц" )
    logo=models.ImageField(upload_to='media',verbose_name='логотип')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'