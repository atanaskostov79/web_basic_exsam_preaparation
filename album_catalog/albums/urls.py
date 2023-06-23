from django.urls import path, include
from .views import *

'''
Routes
• http://localhost:8000/ - home page
• http://localhost:8000/album/add/ - add album page
• http://localhost:8000/album/details/<id>/ - album details page
• http://localhost:8000/album/edit/<id>/ - edit album page
• http://localhost:8000/album/delete/<id>/ - delete album page
• http://localhost:8000/profile/details/ - profile details page
• http://localhost:8000/profile/delete/ - delete profile page
'''
urlpatterns = [
    path('', home_page, name='home'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='album edit'),
    path('album/delete/<int:pk>/', delete_album, name='album delete'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),

]