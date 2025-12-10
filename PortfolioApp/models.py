from django.db import models

class ProjectData(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_used = models.CharField(max_length=200)
    github = models.URLField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)  
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SocialMedia(models.Model):
    github = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()
