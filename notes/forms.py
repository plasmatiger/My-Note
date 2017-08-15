from django import forms
from django.contrib.auth.models import User
#from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets                                       


from .models import *

class Note(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['Tag', 'Note']
################ Event Form #################
class EventForm(forms.ModelForm):
    #event_date = forms.DateField(widget=SelectDateWidget)
    start_date = forms.DateField(widget=SelectDateWidget)
    end_date = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Event
        fields = ['Tag', 'Description']
        #fields[2].widget = widgets.AdminSplitDateTime()

class EventDateEditForm(forms.Form):
    #event_date = forms.DateField(widget=SelectDateWidget)
    start_date = forms.DateField(widget=SelectDateWidget)
    end_date = forms.DateField(widget=SelectDateWidget)
    
    
################ FILE HANDELING ####################
class ImageForm(forms.ModelForm):
    class Meta:
       model = Images
       fields = ['Image_tag', 'Image']

class DocumentForm(forms.ModelForm):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    class Meta:
        model = Document
        fields = ['docfile']
           