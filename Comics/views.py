import json
import os
import re
import base64
import numpy as np


from PIL import Image, ImageFilter
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from WebServerComics.settings import MEDIA_ROOT
from .forms import ImageFormOriginal
from .models import UploadOriginal, UploadBlur, UploadColor, UploadEdge


def index(request):
    return render(request, 'Comics/startpage.html')


def detail(request, image_id):
    image = UploadOriginal.objects.get(pk=image_id)
    template = loader.get_template('Comics/index.html')
    context = {
        'image': image,
    }
    return HttpResponse(template.render(context, request))


def toSaveOriginal(request):

    originImage = UploadOriginal()
    if request.method == 'POST':
        if request.is_ajax():
            form = ImageFormOriginal(request.POST, request.FILES)
            if form.is_valid():
                originImage = UploadOriginal(pk=1, image=request.FILES['image'])
                # originImage.save()
    else:
        form = ImageFormOriginal()

    id, image = change_image(originImage.image, request.FILES['image'])
    opened = open(os.path.join(MEDIA_ROOT, str(image)), 'rb')
    image_read = opened.read()
    image_64_encoded = base64.encodebytes(image_read)

    data = {'image': str(image_64_encoded, encoding='utf-8'), 'id': str(id)}
    return HttpResponse(json.dumps(data), content_type='application/json')


def change_image(uploaded, name):
    file_content = ContentFile(uploaded.read())

    blurImage = UploadBlur(pk=2, image=name)
    blurImage.save()

    new_image_blured = Image.open(file_content)
    im1 = new_image_blured.filter(ImageFilter.CONTOUR)
    im1.save(os.path.join(MEDIA_ROOT, str(blurImage.image)))

    blurImage.save()

    return blurImage.id, blurImage.image


def toSaveColor(request):

    data = {'color': request.POST['color'], 'edge': request.POST['edge']}
    return HttpResponse(json.dumps(data), content_type='application/json')