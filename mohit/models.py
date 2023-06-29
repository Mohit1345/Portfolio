from django.db import models



# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=1000)
    tags = models.CharField(max_length=100)
    Domain = models.CharField(max_length=50)
    link = models.CharField(max_length=150,null=True,blank=True)
    video_link = models.CharField(max_length=500,null=True,blank=True)
    image = models.FileField(null=True,blank=True)
    tagline = models.CharField(max_length=75,null=True,blank=True)
    # Domain = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    # class Meta:
    #     unique_together = ('name')




class Featured_projects(models.Model):
    # Featured_project = models.ForeignKey(Projects,on_delete=models.CASCADE,unique=True)
    Featured_project = models.OneToOneField(Projects,on_delete=models.CASCADE)
    tagline = models.CharField(max_length=75,blank=True,null=True)


    
    def __str__(self):
        return self.Featured_project.name




class Research(models.Model):
    RESEARCH_TYPE_CHOICES = [
        ('P', 'Patent'),
        ('B', 'Featured in book'),
        ('RP', 'Research paper'),
        ('RV', 'Review paper'),
    ]

    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=10000,null=True,blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)
    research_type = models.CharField(max_length=100, choices=RESEARCH_TYPE_CHOICES)
    publication = models.CharField(max_length=100)

    def __str__(self):
        return self.title