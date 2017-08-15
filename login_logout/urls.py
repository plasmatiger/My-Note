from django.conf.urls import url
from . import views

app_name = "login_logout"

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$',views.register,name='register'),
	url(r'^registerform/$', views.register_form, name='register_form'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^filluserdata/$',views.filluserdata, name='filluserdata'),
    url(r'^homepage/$',views.homepage,name='homepage'),
    url(r'^aboutme/$', views.aboutme,name='aboutme'),
]