from django.db import models
from account.models import Account
from datetime import date


class Candidate(models.Model):
    candidate_id = models.IntegerField(blank=False,null=False,primary_key=True)
    info = models.ForeignKey(Account, related_name='candidate', on_delete=models.CASCADE)
    message = models.TextField(null=False,blank=False) 



class Election(models.Model):
    election_id = models.TextField(max_length=5,blank=False,null=False,primary_key=True)
    title = models.CharField(max_length=255,blank=False,null=False)
    candidates = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    started = models.BooleanField(blank=True,null=True)
    start_date = models.DateField(auto_now=False,blank=False,null=False)
    end_date = models.DateField(auto_now=False,blank=False,null=False)

    class Meta:
        ordering = ('-date_created',)

    def has_started(self):
        if self.started or self.start_date == date.today():
            return True
        else:
            return False

    def save(self,*args,**kwargs):
        if self.has_started():
            self.started = True
        super().save(*args,**kwargs)
        




class Vote(models.Model):
    voter = models.ForeignKey(Account, related_name='voter', on_delete=models.CASCADE)
    election = models.ForeignKey(Election, related_name='election', on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, related_name='candidate', on_delete=models.CASCADE)
    date_voted = models.DateTimeField(auto_now=True)