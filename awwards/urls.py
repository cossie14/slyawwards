  
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'api/user/user-id/(?P<pk>[0-9]+)/$',
        views.UserDescription.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view()),
    url(r'^profile/',views.profile,name='profile'),
    url('^$',views.index,name ='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^user/',views.user,name ='user'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api/profile/', views.UserList.as_view()),
    url(r'^api/project/', views.ProjectList.as_view()),

    url(r'^project/',views.new_project,name ='newproject'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    
