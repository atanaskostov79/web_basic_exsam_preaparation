from django.shortcuts import render
from .forms import AlbumForm, ProfileForm
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
            add_album(request)
            return render(request, 'home-no-profile.html', context)

    if get_user_profile():
        return render(request, 'home-with-profile.html', context)

    return render(request, 'home-no-profile.html', context)

def add_album(request):
    context = {
        'form': AlbumForm(),
    }
    return render(request, 'add-album.html', context)

def album_details(request, pk):
    return render(request, 'album-details.html')

def edit_album(request, pk):
    return render(request, 'edit-album.html')

def delete_album(request, pk):
    return render(request, 'delete-album.html')
