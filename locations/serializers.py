import datetime
from rest_framework import serializers
from datetime import datetime
from .models import Point, Track
import time


class CustomField(serializers.Field):

    def to_representation(self, obj):
        return time.mktime(obj.timetuple())

    def to_internal_value(self, obj):
        return datetime.fromtimestamp(obj/1000)


class PointSerializer(serializers.ModelSerializer):
    # dateCreated = CustomField()

    class Meta:
        model = Point
        fields = ('uuid', 'track_uuid', 'lat', 'lng', 'accuracy', 'dateCreated', 'speed',)






class TrackSerializer(serializers.ModelSerializer):
    points = PointSerializer(many=True)
    # dateCreated = CustomField()
    # dateClosed = CustomField()

    class Meta:
        model = Track
        fields = ('uuid', 'owner', 'distance', 'dateCreated', 'dateClosed','dateUpdated', 'comments', 'type', 'status', 'points' )

    def create(self, validated_data):
        points_data = validated_data.pop('points')
        track = Track.objects.create(**validated_data)
        for point_data in points_data:
            Point.objects.create(track=track, **point_data)
        return track



