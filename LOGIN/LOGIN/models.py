from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed

class Person1(models.Model):
    Email=models.CharField(max_length=150)
    Password=models.CharField(max_length=150)
    Username=models.CharField(max_length=150)
    Name=models.CharField(max_length=150)
    DateOfBirth=models.CharField(max_length=150)
    Age=models.IntegerField ()
    District=models.CharField(max_length=150)
    State=models.CharField(max_length=150)
    Occupation=models.CharField(max_length=150)
    About=models.CharField(max_length=150)
    Gender=models.CharField(max_length=1)
    MaritalStatus=models.CharField(max_length=150)

    def save(self):
        super().save()

def user_form(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
        instance.Person.save()

class Feed1(models.Model):
    class Meta:
        db_table = 'Feed'
    Title = models.CharField(max_length=255, blank=True)
    Message = models.CharField(max_length=255, blank=True)
    Photo = models.ImageField(upload_to ='images/')
    Video = models.FileField(upload_to='uploads/', null=True)
    Graph = models.FileField(upload_to='uploads/')

    def showvideo(request):

        lastvideo= Video.objects.last()
        videofile= lastvideo.videofile
    
        form= SharingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        context= {'videofile': videofile, 'form': form}

        return render(request, 'LOGIN/sharing.html', context)
    #def __str__(self):
       # return self.Message + ": " + str(self.videofile)

class Group1(models.Model):
    class Meta:
        db_table = 'Group'
    Name = models.CharField(max_length=150)
    About = models.CharField(max_length=1000)
    Media = models.FileField(upload_to='uploads/',default="")
    

class Booking1(models.Model):
    class Meta:
        db_table = 'Booking'   
    Name = models.CharField(max_length=150)
    ProgrammeName = models.CharField(max_length=150,default="")
    Date = models.DateField()
    Session = models.CharField(max_length=150)

class Workshop1(models.Model):
    class Meta:
        db_table = 'Workshop'
    ProgrammeName = models.CharField(max_length=150,default="")
    Description=models.CharField(max_length=150,default="")
    Date = models.DateField()
    Session = models.CharField(max_length=150)

class SensorData1(models.Model):
    class Meta:
        db_table = 'SensorData'    
    Detail = models.CharField(max_length=255)
    Name = models.CharField(max_length=150)

class Plants1(models.Model):
    class Meta:
        db_table = 'Plants'
    Pictures = models.ImageField(upload_to='uploads/')
    Species = models.CharField(max_length=150)
    Types = models.CharField(max_length=150)

class Comment1(models.Model):
    class Meta:
        db_table = 'Comment'    
    Message = models.CharField(max_length=255)
    Pictures = models.ImageField(upload_to='uploads/')
    Video = models.FileField(upload_to='uploads/')













































