from cloudinary.models import CloudinaryField
from django.db import models
from Account.models import IconList
from mdeditor import fields as md_fields
from autoslug import AutoSlugField
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class Projects(models.Model):
    title = models.TextField(max_length=100)
    explanation = models.TextField()
    detailed_explanation = RichTextField(default=None, blank=True, null=True)
    thumbnail = CloudinaryField("thumbnail",
        width_field='800',
        height_field='533',
        overwrite=True,
        folder='portfolyo/post',
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="webp",)
    technologies = models.ManyToManyField('projects.Technologies')
    view = models.ManyToManyField('base.ViewModel')
    github_url = models.URLField(default='https://github.com/F4ruk-seker')
    slug = AutoSlugField(
        populate_from='title',  # Use 'name' field to populate the slug
        slugify=slugify,  # Use the slugify function from Django's utils
        always_update=True
    )

    def get_technologies(self):
        return self.technologies.all()

    def get_best_used_technologies(self) -> str:
        result_text = ''
        technologies = self.technologies.all()
        sorted_technologies = technologies.order_by('-priority')
        for technology in sorted_technologies:
            result_text += technology.name[:5] + ','
        if technologies.count() > 3: result_text += '...'
        return result_text


class Technologies(IconList):
    def __str__(self):
        return str(self.name)


# from projects.models import Projects
#
# a = Projects.objects.first()
# a.get_best_used_technologies()
