from django.shortcuts import render, redirect
from .forms import AlbumForm, ProfileForm, AlbumDeleteForm
from .models import Profile, Album
# Create your views here.
def get_user_profile():
    try:
        return Profile.objects.all()
    except:
        return None
def home_page(request):
    context = {
        'form': ProfileForm()
    }
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'home-with-profile.html', context)

    if get_user_profile():
        albums = Album.objects.all()
        context = { 'albums': albums }
        return render(request, 'home-with-profile.html', context)

    return render(request, 'home-no-profile.html', context)

def add_album(request):

    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': AlbumForm(),
    }
    return render(request, 'add-album.html', context)

def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {'album': album}
    return render(request, 'album-details.html', context)

def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm(instance=album)
    context = {
        'form': form,
        'album': album
    }
    print(context['form'])
    return render(request, 'edit-album.html', context)

def delete_album(request, pk):
    form = AlbumDeleteForm(request.POST or None, instance=Album.objects.get(pk=pk))
    return render(request, 'delete-album.html')
