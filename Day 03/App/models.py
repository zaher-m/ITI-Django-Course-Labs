from django.db import models
    
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    published = models.DateField()
    auther = models.ForeignKey(Author, on_delete=models.CASCADE)
    appropreiate = models.CharField(choices=(
        ("under 8", "8"),
        ("8-15", "8-15"),
        ("adults", "+15")
        ))

    def __str__(self):
        return self.title