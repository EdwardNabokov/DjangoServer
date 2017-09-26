from django.db import models
from PIL import Image


class UploadOriginal(models.Model):
    image = models.ImageField(upload_to='original')


class UploadBlur(models.Model):
    image = models.ImageField(upload_to='blur')


class UploadEdge(models.Model):
    image = models.ImageField(upload_to='edge')


class UploadColor(models.Model):
    image = models.ImageField(upload_to='color')


