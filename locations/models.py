import datetime
from django.db import models
import datetime
import time
# Create your models here.
from authentication.models import Profile
from django.contrib.auth.models import User


class Track(models.Model):

    # public static final int TRACK_OPENED = 0;
    # public static final int TRACK_CLOSED = 1;
    #
    # public static final int TYPE_CAR = 40;
    # public static final int TYPE_BIKE = 50;
    # public static final int TYPE_FOOT = 60;


    uuid = models.UUIDField(null=True)
    distance = models.FloatField(null=True)
    dateCreated = models.DateTimeField(null=True)
    dateClosed = models.DateTimeField(null=True)
    dateUpdated = models.DateTimeField(null=True)
    comments = models.TextField(null=True, blank=True)
    type = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    profile = models.ForeignKey(Profile, null=True)
    owner = models.TextField(null=True)


    class Meta:
            ordering = ('dateCreated',)




    # List<Point> points;
    # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))

class Point(models.Model):

    uuid = models.UUIDField(null=True)
    track_uuid = models.UUIDField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    accuracy = models.FloatField(null=True)
    dateCreated = models.DateTimeField(null=True)
    speed = models.FloatField(null=True)
    track = models.ForeignKey(Track, related_name='points')


    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.uuid, self.track_uuid)