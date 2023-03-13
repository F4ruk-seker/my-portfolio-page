from cloudinary.models import CloudinaryField
from django.db import models
from Account.models import IconList

class Projects(models.Model):
    title = models.TextField(max_length=100)
    explanation = models.TextField()
    thumbnail = CloudinaryField("avatar",
        width_field='800',
        height_field='533',
        overwrite=True,
        folder='portfolyo/post',
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="webp",)
    technologies = models.ManyToManyField('projects.Technologies')
    github_url = models.URLField(default='https://github.com/F4ruk-seker')


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
