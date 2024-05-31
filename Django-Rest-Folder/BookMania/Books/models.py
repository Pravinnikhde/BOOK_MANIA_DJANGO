from django.db import models



class BookModel(models.Model):
    bookname=models.CharField(max_length=100)
    authname=models.CharField(max_length=100)
    description=models.CharField(max_length=1000000)


    def __str__(self):
        return self.authname
        