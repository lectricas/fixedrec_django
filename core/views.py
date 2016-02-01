from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import loader, RequestContext

# Create your views here.
from locations.models import Track
from django.core.urlresolvers import reverse as r
from django.shortcuts import render
from django.utils.html import escape
from django.contrib.auth.models import User

from activities.models import Activity


def get_following_feeds(user):
    feeds = []
    try:
        activities = []
        followers = Activity.objects.filter(to_user=user, activity_type=Activity.FOLLOW)
        for follower_user in followers:
            activities.append(follower_user)
        following = Activity.objects.filter(from_user=user, activity_type=Activity.FOLLOW)
        for following_user in following:
            activities.append(following_user)
            initial_activity = Activity.objects.get(from_user=user, to_user=following_user.to_user, activity_type=Activity.FOLLOW)
            following_user_activities = Activity.objects.filter(from_user=following_user.to_user, activity_type=Activity.FOLLOW, date__gte=initial_activity.date).exclude(to_user=user)
            for activity in following_user_activities:
                activities.append(activity)
        activities.sort(key=lambda a: a.date, reverse=True)
        for activity in activities:
            if activity.from_user == user:
                activity.message = u'<a href="{0}">You</a> are now following <a href="{1}">{2}</a>'.format(
                    r('reviews', args=(user.username,)),
                    r('reviews', args=(activity.to_user.username,)),
                    escape(activity.to_user.profile.get_screen_name())
                    )
            else:
                is_following = activity.to_user.profile.get_screen_name()
                if activity.to_user == user:
                    is_following = u'you'
                activity.message = u'<a href="{0}">{1}</a> is now following <a href="{2}">{3}</a>'.format(
                    r('reviews', args=(activity.from_user.username,)),
                    escape(activity.from_user.profile.get_screen_name()),
                    r('reviews', args=(activity.to_user.username,)),
                    escape(is_following)
                    )
            feeds.append(activity)
    except Exception as e:
        pass
    return feeds


def profile(request, username):
    user = get_object_or_404(User, username__iexact=username)
    followers = user.profile.get_followers()
    is_following = False
    if request.user in followers:
        is_following = True

    followers_count = user.profile.get_followers_count()
    following_count = user.profile.get_following_count()


    context = RequestContext(request, {
        'page_user': user,
        'is_following': is_following,
        'following_count': following_count,
        'followers_count': followers_count
        })
    return render_to_response('core/profile.html', context)

def home(request):
    if request.user.is_authenticated():
        return redirect(global_map)
    else:
        return render(request, 'core/cover.html')


def global_map(request):
    return render(request, 'core/global_map.html')

def get_tracks(user):
    return user.profile.track_set.all();

def tracks(request, username=None):
    if username:
        user = get_object_or_404(User, username__iexact=username)
    else:
        user = request.user

    tracks = user.profile.track_set.all()
    return render(request, 'core/tracks.html', {'tracks': tracks})


# def reviews(request, username):
#     user = get_object_or_404(User, username__iexact=username)
#     followers = user.profile.get_followers()
#     is_following = False
#     if request.user in followers:
#         is_following = True
#
#     followers_count = user.profile.get_followers_count()
#     following_count = user.profile.get_following_count()
#
#     user_reviews = user.profile.get_reviews()
#
#     context = RequestContext(request, {
#         'user_reviews': user_reviews,
#         'page_user': user,
#         'is_following': is_following,
#         'following_count': following_count,
#         'followers_count': followers_count
#         })
#     return render_to_response('reviews/reviews.html', context)


def messaging(request):
    return render(request, 'core/messaging.html')

def feed(request):
    return render(request, 'core/feed.html')
