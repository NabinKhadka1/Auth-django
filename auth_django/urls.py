from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('passchange/',views.user_passchange,name='passchange'),
    path('passchange1/',views.user_passchange1,name='passchange1'),
    path('user-detail/<int:id>/',views.user_detail,name='userdetail'),

]
