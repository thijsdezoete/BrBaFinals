from django.db import models


class Contestant(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Contestants"

    def __unicode__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Breaking Bad Characters"

    def __unicode__(self):
        return self.name

class Result(models.Model):
    name = models.ForeignKey('Contestant')
    character = models.ForeignKey('People', related_name="choice", blank=True, null=True)
    is_survivor = models.BooleanField(default=True)
    killed_by = models.ForeignKey('People', blank=True, null=True)

    def __unicode__(self):
        return str(self.name) + " answer for " + str(self.character)
