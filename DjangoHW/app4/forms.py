from django import forms


class ImgProductUpload(forms.Form):
    img = forms.ImageField()
