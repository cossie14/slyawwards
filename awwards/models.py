from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    profile_picture = models.ImageField(upload_to ='profile/')
    username = models.CharField(max_length =60,primary_key=True)
    bio = HTMLField()
    user_id = models.IntegerField(default=0)
    contact = models.BigIntegerField()
    


    def __str__(self):
        return self.username
    '''save profile method'''
    def save_profile(self):
        self.save()

    '''delete ratings method'''
    def delete_profile(self):
        deleted_profile = Profile.objects.all().delete()
        return deleted_profile

    

 
class Project(models.Model):
    title = models.CharField(max_length=60)
    project_posts = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    project_pic = models.ImageField(upload_to='project/', blank=True)
    project_url = models.URLField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    def save_Project(self):
        self.save()


    def get_absolute_url(self):
        return reverse('dump', kwargs={'pk':self.pk})


    def __str__(self):
        return self.title

    @classmethod
    def all_projects(cls):
        project = cls.objects.order_by('pub_date')
        return project

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__title__icontains=search_term)
        return project

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


