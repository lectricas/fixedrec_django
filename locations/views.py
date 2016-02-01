from django.http import HttpResponse
from djoser.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework import permissions
from locations.permissions import  IsOwner


from locations.models import Track
from locations.serializers import TrackSerializer
from rest_framework import generics
from django.contrib.auth.models import User

from datetime import datetime




class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


            # curl -H "Authorization: Token ce7950e8d0c266986b7f972407db89881032228e" http://127.0.0.1:8000/auth/me/


@permission_classes(permissions.IsAuthenticated,)
@api_view(['GET', 'POST'])
def track_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tracks = request.user.profile.track_set.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=request.user.profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def last_update_iso(request, last_update_iso):
    return HttpResponse(last_update_iso)



@permission_classes(permissions.IsAuthenticated,)
@api_view(['GET', 'POST'])
def new_track_list(request, last_update=0):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        last_update = datetime.fromtimestamp(float(last_update)/1000)
        # tracks = request.user.profile.track_set.all()
        tracks = Track.objects.filter(profile_id = request.user.profile.id, dateClosed__gt = last_update)
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=request.user.profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




@api_view(['GET', 'PUT', 'DELETE'])
def track_detail(request, uuid):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        track = Track.objects.get(uuid=uuid)
    except Track.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrackSerializer(track)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

