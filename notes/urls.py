from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^hello/', views.hello, name='hello'),
    url(r'^enternoteform/', views.enterNoteform, name='enterNoteform'),
    url(r'^printNote/', views.enterNote, name='printNote'),
    url(r'^displaynote/(\d+)/', views.displayNote, name='displaynote'),
    #
    url(r'^searchTag/(\w+)/', views.searchTag, name = 'searchTag'),
    #
    url(r'^editNoteform/(\d+)/', views.editNoteform, name = 'editNoteform'),
    url(r'^editNote/(\d+)/', views.editNote, name = 'editNote'),
    url(r'^deleteNote/(\d+)/', views.deleteNote, name = 'deleteNote'),
    url(r'^searchNote/', views.searchNote, name='searchNote'),
    #url(r'^search/', views.search, name='search'),
    url(r'^alltags/', views.AllTags, name = 'AllTags'),
    #
    url(r'^image/', views.Image, name = 'Image'),
    url(r'^saved/', views.Display, name = 'Display'),
    #url(r'^saved/', views.saved, name = 'Display')
    url(r'^upload/', views.uploadDocument, name = 'upload'),
    url(r'^savedoc/', views.saveDoc, name='saveDoc'),
    url(r'^listdocs/$', views.listDocs, name='listdoc'),
    #
    url(r'^calendar/(\d+)/(\d+)', views.calendarof, name='calendarof'),
    url(r'^calendar/', views.calendar, name='calendar'),
    #
    url(r'^enterevent/', views.enterEventForm, name='enterevent'),
    url(r'^saveEvent/', views.saveEvent, name='saveEvent'),
    #
    url(r'^editEventform/(\d+)/', views.editEventform, name = 'editEventform'),
    url(r'^editEvent/(\d+)/', views.editEvent, name = 'editEvent'),
    url(r'^deletEvent/(\d+)/', views.deleteEvent, name = 'deleteEvent'),
    url(r'^allevents/', views.allevents, name='allevents'),
    #url(r'^searchNote/', views.searchNote, name='searchNote'),
    #
    url(r'^deleteDoc/(\d+)/', views.deleteDoc, name = 'deleteDoc'),
]