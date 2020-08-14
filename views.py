from django.shortcuts import render_to_response
from models import Contacts

# Create your views here.
def contacts(request):
	contacts_list = Contacts.objects.all()
	return render_to_response('contacts_list.html', {'contacts_list': contacts_list}) 

