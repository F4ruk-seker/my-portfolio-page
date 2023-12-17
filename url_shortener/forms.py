from django import forms
from .models import UrlModel
from django.utils.text import slugify


class UrlShorterForm(forms.ModelForm):
    custom_url_path = forms.CharField(max_length=50, required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        custom_url_path = self.cleaned_data.get('custom_url_path')
        for tr_k, eng_k in [
            ('ş', 's'),
            ('ı', 'i'),
            ('ç', 'c'),
            ('ğ', 'g'),
            ('ü', 'u'),
        ]:
            custom_url_path.replace(tr_k.upper(), eng_k.upper())
            custom_url_path.replace(tr_k, eng_k)
        if custom_url_path:
            instance.router_url = slugify(custom_url_path)
        else:
            if not instance.router_url:
                instance.router_url = instance.create_random_router()
        if commit:
            instance.save()
        return instance

    class Meta:
        model = UrlModel
        # fields = '__all__'
        exclude = ('router_url', )
