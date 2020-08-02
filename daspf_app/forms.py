from django import forms

from daspf_app.models import Post, PostImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'category',
            'image',
        ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PostImage
        fields = [
            'image'
        ]


class PostFullForm(PostForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ['images']


class PageDataForm(forms.Form):
    title = forms.CharField(required=True, label='Titlu', widget=forms.TextInput(
        attrs={"class": "w-100 my-2"}
    ))
    body = forms.CharField(required=True, label='Conținut postare', widget=forms.Textarea(attrs={
        "class": "my-2 w-100",
    }))
    # photo = CroppieField()
