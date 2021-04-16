from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_category():
        return Category.objects.all()