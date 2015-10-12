from django.db import models

# Create your models here.


class StateCapital(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    # state = models.ForeignKey('main.State', null=True, blank=True)
    # state = models.ManyToManyField('main.State')
    state = models.OneToOneField('main.State', null=True, blank=True)

    def __unicode__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    abbrev = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name


class City(models.Model):
    zipc = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    lon = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    abbrev = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    state = models.ForeignKey('main.State', null=True, blank=True)

    # override the save method implemented in the city_create view
    def save(self, *args, **kwargs):
        state_s = State.objects.get(name=self.state)
        self.abbrev = state_s.abbrev
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'cities'

    def __unicode__(self):
        return self.name
