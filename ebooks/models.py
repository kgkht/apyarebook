from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=220)
    summary = models.CharField(max_length=2083)

    def __str__(self):
        return self.name
    

class Ebook(models.Model):
    name = models.CharField(max_length=250)
    summary = models.CharField(max_length=2083)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    source_file = models.FileField(upload_to='pdf/', default='')
    image = models.ImageField(upload_to='images/', default='')
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.name

    def summary_shorthen(self):
        return self.summary[:125]
