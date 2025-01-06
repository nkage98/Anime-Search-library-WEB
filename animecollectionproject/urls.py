from django.contrib import admin
from django.urls import path, include

from animecollectionapp.views import (
    home, anime_info,
)

from account.views import(
    registration_view, 
    login_view, 
    logout_view,
    account_view,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('anime/<anime_id>/', anime_info, name="anime_info"),
    path('account/', account_view, name="account"),

]
