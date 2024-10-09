from django.urls import include, path


from . import views

app_name = 'users'

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),

]
