from django.db import models

# Create your models here.
class MyProject(models.Model) :
    project_name = models.CharField(max_length=200)
    sub_title = models.CharField(max_length= 200,default=None)
    description = models.TextField(default='')
    git_url = models.URLField(default = None)
    prev_url = models.URLField(default = None)
    
    project_image = models.ImageField(upload_to='', blank=True , null = True )


    def __str__(self):
        return self.project_name
