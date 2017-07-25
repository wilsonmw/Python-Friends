from django.conf.urls import url
from . import views
from ..login_app.models import User

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^addFriend$', views.addFriend),
    url(r'^add$', views.add),
    url(r'^show$', views.show),
    url(r'^deleteFriend$', views.deleteFriend),
    url(r'^logout$', views.logout),
]