from django import forms


class ImageFormOriginal(forms.Form):
    image = forms.ImageField(
        label='Select a file',
    )


class ImageFormBlur(forms.Form):
    image = forms.ImageField(
        label='Select a file',
    )


class ImageFormColor(forms.Form):
    image = forms.ImageField(
        label='Select a file',
    )