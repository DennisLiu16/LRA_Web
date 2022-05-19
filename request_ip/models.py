from django.db import models
import ipaddress

class ipInfo(models.Model):
    connected_time = models.DateTimeField('datatime connected')
    server_ipv4 = models.CharField(max_length=15)   # max IPv4 is 15
    usr_ipv4 = models.CharField(max_length=15)

    def __str__(self):
        return self.server_ipv4

    def ip_isValid(self):
        try:
            ip = ipaddress.ip_address(self.server_ipv4)
            if ip.version == 4:
                return True

        except ValueError:
            print('address/netmask is invalid: {}'.format(self.server_ipv4))
        except:
            print('Usage : {}  ip'.format(self.server_ipv4))
