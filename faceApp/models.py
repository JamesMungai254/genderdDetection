from django.db import models



# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=50, default=None)
    img = models.ImageField(upload_to='images/', default=None)
    processed_image = models.ImageField(upload_to='processed/', null=True, blank=True)
    


""""
from django.db import models
from utils import get_filtered_img
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
ACTION_CHOICES =(
    ('NO_FILTER','no filter'),
    ('COLORIZED','colorized'),
    ('GRAYSCALE','grayscale'),
    ('BLURRED','blurred'),
    ('BINARY','binary'),
    ('INVERT','invert')
)

class Upload(models.Model):
    img = models.ImageField(upload_to='images/', default=None)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        #open image
        pil_img=Image.open(self.image)
        #convert image to array and do some processing
        cv_img=np.array(pil_img)
        img = get_filtered_img(cv_img,self.action)
        
        #convert back to pil image
        im_pil=Image.fromarray(img)
        
        #save
        buffer =BytesIO()
        im_pil.save(buffer,format='png')
        image_png = buffer.getvalue
        
        self.image.save(str(self.image),ContentFile(image_png,save=False))
        super().save(*args,**kwargs)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
