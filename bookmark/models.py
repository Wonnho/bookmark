from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    web_site=models.CharField(max_length=110)
    url=models.URLField('Site URL')

    # def __str__(self):
        # return "Web_Site:" + self.web_site ", URL_address:" + self.url

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])