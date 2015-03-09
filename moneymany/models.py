from django.db import models


class Computer(models.Model):
    name = models.CharField(max_length=30)
    paytime = models.IntegerField(default=0)
    happytime = models.IntegerField(default=0)
    image_urls  = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return '%s' % (self.name)


class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    createtime = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()