from django.db import models

from django.db import models
import datetime
import os
from django.contrib.auth.models import User


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%y%M%d%H: %M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


def get_file_path_product(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%y%M%d%H: %M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('product_uploads/', filename)


class category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    # description = models.TextField(max_length=120, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    # meta_title = models.CharField(max_length=150, null=False, blank=False)
    # meta_keyworld = models.CharField(max_length=150, null=False, blank=False)
    # meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path_product, null=True, blank=True)
    is_new = models.BooleanField(default=True)
    quantity = models.IntegerField(null=False, )
    original_price = models.FloatField(null=False, blank=False)
    seling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False)
    tag = models.CharField(max_length=150, null=True, blank=True)
    short_dyscryption = models.TextField(max_length=300, null=True, blank=True)
    long_dyscryption = models.TextField(max_length=700, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

