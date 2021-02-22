from django.db import models


class UserField(models.Model):
    KEY_CHOICES = (
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('linkedin', 'Linkedin'),
        ('instagram', 'Instagram'),
        ('pinterest', 'Pinterest'),
    )
    name = models.CharField(max_length=50, choices=KEY_CHOICES)
    value = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} : {self.value}'


class Service(models.Model):
    sort = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    fa_icon_class = models.CharField(max_length=50)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.title

