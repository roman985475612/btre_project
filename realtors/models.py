from django.db import models


class RealtorManager(models.Manager):

    def get_mvp(self):
        return Realtor.objects.all().filter(is_mvp=True)


class Realtor(models.Model):
    name        = models.CharField(max_length=200)
    photo       = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone       = models.CharField(max_length=20)
    email       = models.EmailField()
    is_mvp      = models.BooleanField(default=False)
    hire_date   = models.DateTimeField(auto_now_add=True)
    objects     = RealtorManager()

    class Meta:
        ordering = ['-hire_date']

    def __str__(self):
        return self.name
