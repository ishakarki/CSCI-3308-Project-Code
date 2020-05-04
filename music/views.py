from django.views import generic
from .models import Album 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm
from .models import Song


def home(request):
	template = loader.get_template('music/home.html')
	context = {}
	return HttpResponse(template.render(context, request))


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

class QueueView(ListView):
	template_name = 'music/queue.html'
	context_object_name = 'all_songs'
	model = Song

	def get_queryset(self):
		return Song.objects.filter(is_upvote = True)



class AlbumCreate(CreateView):
	model = Album
	fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'



	#dispalay blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False) #creates an object from the form, doesn't save to database yet

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password) #hash
			user.save() #save user to database

			#returns User object if credentials are correct
			user = authenticate(username=username, password=password)
			if user is not None:

				if user.is_active:
					login(request,user) #login
					return redirect('music:index')

		return render(request, self.template_name, {'form': form})






def addqueue(request, album_id):
	album = get_object_or_404(Album, pk= album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except(KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {
			'album': album,
			'error_message': "You did not select a valid song",
			})
	else:
		selected_song.is_upvote = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album':album})


		














