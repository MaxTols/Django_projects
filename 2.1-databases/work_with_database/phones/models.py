from django.db import models
from slugify import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)
