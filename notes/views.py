#import utils
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from notes.forms import *
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone#, generic_search
#from django.urls import reverse
from django.core.urlresolvers import reverse
##
from django.shortcuts import render_to_response,redirect
from django.utils.safestring import mark_safe
from datetime import datetime
from .models import WorkoutCalendar,Event
#from haystack.generic_views import SearchView
#from utils import generic_search
################ Custom Views #########################
# used for creating Note form
def enterNoteform(request):
	if request.user.is_authenticated():
		form = Note()
		return render(request, 'enterNote.html', {"form":form})
	else:
		return redirect('login_logout:index')	
# enter a Note that need to be saved
def enterNote(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = Note(request.POST)
			if form.is_valid():
				username = request.user.username
				UserName = User.objects.get(username=username)
				tag = form.cleaned_data['Tag']
				note = form.cleaned_data['Note']
				newNote = Notes(UserName = UserName ,Tag = tag, Note = note)
				#newNote = Notes(Tag = tag, Note = note)
				newNote.save()
				#context = {'Tag' : tag, 'Note' : note,}
				return redirect('notes:AllTags')
			else:
				form = Note()
		return render(request, 'enterNote.html', {"form" : form})
	else:
		return redirect('login_logout:index')
# Editing a Note
def editNoteform(request, id):
	if request.user.is_authenticated():
		note = Notes.objects.get(UserName=request.user,pk=id)
		return render(request, 'editNoteform.html',  {"note" : note})
	else:
		return redirect('login_logout:index')
# save edited note
def editNote(request, id):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = Note(request.POST)
			if form.is_valid():
				note = Notes.objects.get(UserName=request.user,pk=id)
				note.Tag = form.cleaned_data['Tag']
				note.Note = form.cleaned_data['Note']
				note.modified_date = datetime.now()
				note.save()
				#context = {'Tag' : tag, 'Note' : note,}
				#return render(request, 'index.html',)
				return redirect('notes:AllTags')
			else:
				note = Notes.objects.get(UserName=request.user,pk=id)
		return render(request, 'editNoteform.html',  {"note" : note})
	else:
		return redirect('login_logout:index')	
# Deleting a Note
def deleteNote(request, id):
	if request.user.is_authenticated():
		Notes.objects.get(UserName=request.user,pk=id).delete()
		#return HttpResponse("done")
		return redirect('notes:AllTags')
	else:
		return redirect('login_logout:index')	
# Printing all notes under the user
def AllTags(request):
	if request.user.is_authenticated():
		username = request.user.username
		username = User.objects.get(username=username)
		notes = Notes.objects.filter(UserName = username)
		return render(request, 'note.html', {"notes" : notes})
	else:
		return redirect('login_logout:index')
def displayNote(request, id):
	if request.user.is_authenticated():
		note = Notes.objects.get(UserName=request.user,pk=id)
		return render(request, 'printNote.html', {'note' : note})
	else:
		return redirect('login_logout:index')
# Serch a tag given after URL : searchTag/"."
def searchTag(request, tag):
	if request.user.is_authenticated():
		objects = Notes.objects.filter(UserName=request.user,Tag = tag)
		ob ='Printing all Notes with Tag : %s in the DB : <br>'%(tag)
		for tag in objects:
			ob += tag.Note+"<br>"

		return HttpResponse(ob)
	else:
		return redirect('login_logout:index')
# Search Note using Tag from GET request(Partial search accepted)
def searchNote(request):
	if request.user.is_authenticated():
		q = request.GET.get('q', None)
		if q:
			username = request.user.username
			username = User.objects.get(username=username)
			notes = Notes.objects.filter(UserName=username, Tag__contains=q)
			return render(request, 'search.html', {'notes' : notes})
		return HttpResponse("Search Empty")
	else:
		return redirect('login_logout:index')
# Search that search all fields of all models for that object which we have passed as search object
MODEL_MAP = { Notes: ["UserName","Tag","Note","my_date","modified_date"],
              Event  : ["UserName","Tag","Description","event_date","my_date","start_date","end_date",],
            }
# def search(request):
	# objects = []
	# for model,fields in MODEL_MAP.iteritems():
		# objects+=generic_search(request,model,fields,)
		# return render_to_response("search_result.html",
                                 # {"objects":objects,
                                  # "search_string" : request.GET.get('q',""),
                              # }
       # )

	# return HttpResponse("Search Empty")
####################################################
################ Event Scheduling ##################
####################################################
def enterEventForm(request):
	if request.user.is_authenticated():	
		form = EventForm()
		return render(request, 'enter_event.html', {"form":form})
	else:
		return redirect('login_logout:index')
# save event
def saveEvent(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EventForm(request.POST)
			if form.is_valid():
				#print "its ok"
				username = request.user.username
				UserName = User.objects.get(username=username)
				tag = form.cleaned_data['Tag']
				description = form.cleaned_data['Description']
				#eventdate = form.cleaned_data['event_date']
				startdate = form.cleaned_data['start_date']
				enddate = form.cleaned_data['end_date']
				newEvent = Event(
					UserName = UserName ,
					Tag = tag, 
					Description = description,
					start_date = startdate,
					end_date = enddate)
				newEvent.save()
				######## just for verification 
				#context = {'UserNmae' : UserName, 'Tag' : tag, 'Note' : description,}
				#return render(request, 'printNote.html', context)
				return redirect('notes:allevents')
			else:
				form = EventForm()
				#return HttpResponse("Nope")
		return render(request, 'enterNote.html', {"form" : form})
	else:
		return redirect('login_logout:index')
# Editing a event
def editEventform(request, id):
	if request.user.is_authenticated():
		event = Event.objects.get(UserName=request.user,pk=id)
		form = EventDateEditForm(initial={'start_date' : event.start_date, 'end_date' : event.end_date})
		#return HttpResponse("success")
		return render(request, 'editEventform.html',  {"event" : event, "form" : form })
	else:
		return redirect('login_logout:index')	
# save edited note
def editEvent(request, id):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EventForm(request.POST)
			if form.is_valid():
				event = Event.objects.get(UserName=request.user,pk=id)
				event.Tag = form.cleaned_data['Tag']
				event.Description = form.cleaned_data['Description']
				#event.event_date = form.cleaned_data['event_date']
				event.start_date = form.cleaned_data['start_date']
				event.end_date = form.cleaned_data['end_date']
				#print date
				event.save()
				#context = {'Tag' : tag, 'Note' : note,}
				return render(request, 'index.html',)
			else:
				event = Event.objects.get(UserName=request.user,pk=id)
				form = EventDateEditForm(initial={'start_date' : event.start_date, 'end_date' : event.end_date})
		return render(request, 'editEventform.html',  {"event" : event, "form" : form })
	else:
		return redirect('login_logout:index')	
# Deleting a Note
def deleteEvent(request, id):
	if request.user.is_authenticated():
		Event.objects.get(UserName=request.user,pk=id).delete()
		return redirect('notes:allevents')
	else:
		return redirect('login_logout:index')
# Printing all events under the user
def allevents(request):
	if request.user.is_authenticated():
		events = Event.objects.filter(UserName=request.user).order_by('start_date')
		return render(request, 'allevents.html', {'events' : events})
	else:
		return redirect('login_logout:index')	
# Serch a tag given after URL : searchTag/"."

# Search Note using Tag from GET request(Partial search accepted)

################ FILE HANDELING ####################
########## Image Uploading #######
# used to create image form
def Image(request):
	if request.user.is_authenticated():
		form = ImageForm()
		return render(request, 'image.html', {'form':form})
	else:
		return redirect('login_logout:index')
# saving image and replying using HttpResponse
def Display(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = ImageForm(request.POST, request.FILES)
			if form.is_valid():
				profile = Images()
				username = request.user.username
				user = User.objects.get(username=username)
				profile.UserName = user
				profile.Image_tag = form.cleaned_data["Image_tag"]
				profile.Image = form.cleaned_data["Image"]
				profile.save()
				#return render(request,'saved.html',)
				return HttpResponse("Saved Image")
			else:
				form = ImageForm()
		return render(request, 'image.html', {'form': form} )
	else:
		return redirect('login_logout:index')
##########################################
#
############ Doc Uploading ###############
# used to create doc upload form
def uploadDocument(request):
	docform = DocumentForm()
	return render(request, 'upload.html', {'form': docform } )
# saving a doc and redirecting for another upload
def saveDoc(request):
	# Handle file upload
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = DocumentForm(request.POST, request.FILES)
			if form.is_valid():
				#print request.FILES['docfile'].
				#user = User.objects.get(username=request.user.username)
				newdoc = Document(UserName = request.user, docfile = request.FILES['docfile'])
				newdoc.save()
				savestatus = "Doc saved successfully. You can Procced further"
				form = DocumentForm()
				return render(request, 'upload.html', {'savestatus' : savestatus, 'form' : form})
			else:
				form = DocumentForm() # A empty, unbound form
		return render(request, 'upload.html', {'form': form})
	else:
		return redirect('login_logout:index')
# Deleting a Note
def deleteDoc(request, id):
	if request.user.is_authenticated():
		Document.objects.get(UserName=request.user,pk=id).delete()
		return redirect('notes:listdoc' )
	else:
		return redirect('login_logout:index')
# listing all the docs under the user
def listDocs(request):
	if request.user.is_authenticated():
		#UserName = User.objects.get(username=request.user)
		documents = Document.objects.filter(UserName = request.user)
		return render(request, 'listDocs.html', {'docs' : documents})
	else:
		return redirect('login_logout:index')

###################### HTML Calender ################
def calendarof(request, year, month):
	if request.user.is_authenticated():	
		today = datetime.now().date()
		year = int(year)
		month = int(month)
		if month > 12 :
			month = 01
			year+=1
		if month < 01 :
			month = 12
			year -= 1
		#events = Event.objects.order_by('start_date','my_date').all()
		events = Event.objects.order_by('start_date','my_date').filter(
			UserName=request.user,
			start_date__year__lte=year, 
			start_date__month__lte=month,
			end_date__year__gte=year,
			end_date__month__gte=month,
			)

		cal = WorkoutCalendar(events).formatmonth(year, month)

		return render_to_response('calendar.html', {'calendar': mark_safe(cal), "Event" : events, "year" : year, "previous":month-1, "next":month+1})
	else:
		return redirect('login_logout:index')	

def calendar(request):
	if request.user.is_authenticated():	
		today = datetime.now().date()
		
		year = today.year
		month = today.month	
		#
		#events = Event.objects.order_by('start_date','my_date').all()
		events = Event.objects.order_by('start_date','my_date').filter(
			UserName=request.user,
			start_date__year__lte=year, 
			start_date__month__lte=month,
			end_date__year__gte=year,
			end_date__month__gte=month,
			)

		cal = WorkoutCalendar(events).formatmonth(year, month)

		return render_to_response('calendar.html', {'calendar': mark_safe(cal), "Event" : events, "year" : year, "previous":month-1, "next":month+1})
	else:
		return redirect('login_logout:index')	


