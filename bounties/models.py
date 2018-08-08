from django.db import models
from django.utils import timezone

class Bounty(models.Model):
    company = models.CharField(max_length=255, null=True)  # TODO: replace with foreign key: Company
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=4000, null=True)  # TODO: make this stuff more detailed
    size = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    created = models.DateTimeField(default=timezone.now, null=True)
    status_code = models.IntegerField(null=True, default=-1)
    
    status_code_dict = {-1:'Not set',
                        0:'Created',
                        1:'Alive',
                        2:'Withdrawn',
                        3:'Realized'}    
    
    def __unicode__(self):
        return(self.title)
    
    def status(self):
        '''Print status'''
        return(self.status_code_dict[self.status_code])