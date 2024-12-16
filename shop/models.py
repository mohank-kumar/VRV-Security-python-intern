from django.db import models
import datetime
import os

def getFileName(request,filename):
    now_time = datetime.datetime.now().strftime( "%d/%m/%Y, %H:%M:%S")
    new_FileName = '%s%s'%(now_time,filename)
    return os.path.join('uploads/' , new_FileName)

class catagory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    state = models.BooleanField(default=False,help_text='0-show,1-hidden')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.name

class product(models.Model):
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    original_price =models.FloatField(null=False,blank=False)
    selling_price =models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    state = models.BooleanField(default=False,help_text='0-show,1-hidden')
    trending = models.BooleanField(default=False,help_text='0-default,1-trending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name
   