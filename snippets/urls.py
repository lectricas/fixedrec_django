from django.conf.urls import url
from snippets import views

urlpatterns = [
    # url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/$', views.snippet_list),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]




