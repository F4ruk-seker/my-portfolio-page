from django.db import models


class Certificate(models.Model):
    name = models.TextField()
    technologies = models.ManyToManyField('projects.Technologies')
    certificate_id = models.TextField(default=None,null=True)
    verification = models.TextField(null=True)
    organisation = models.ManyToManyField('Portfolyo.Organisation')
    priority = models.IntegerField()
    date = models.DateField(null=True)


class Organisation(models.Model):
    name = models.TextField()
    url = models.URLField()


class Education(models.Model):
    name = models.TextField()
    url = models.URLField()
    # logo = models.ImageField()
    profession = models.TextField()


class Experience(models.Model):
    name = models.TextField()
    description = models.TextField()
    organisation = models.ManyToManyField('Portfolyo.Organisation')
