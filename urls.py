from django.conf.urls import url
from django.contrib import admin
from addressbook.views import contacts
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^show/', contacts)
]