from django.db import models

class ipInfo(models.Model):
    connected_time = models.DateTimeField('datatime connected')
    server_ipv4 = models.CharField(max_length=15)   # max IPv4 is 15
    usr_ipv4 = models.CharField(max_length=15)
