from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
	return render(request,'generator/home.html')
def password(request):
	l=list()
	#length=10
	if request.GET.get('lowercase'):
		l.extend(list('abcdefghijklmnopqrstuvwxyz'))
	
	if request.GET.get('numbers'):
		l.extend(list('1234567890'))
	if request.GET.get('specialchars'):
		l.extend(list('!@#$%^&*()_+'))
	if request.GET.get('uppercase'):
		l.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
	length=int(request.GET.get('length'))
	

	password=''
	if length==0:
		return HttpResponse("Warning: password can not be empty! Choose the content")
	else:
		for i in range(length):
			password+=random.choice(l)
		return render(request,'generator/password.html',{'password':password,'len':length})

def about(request):
	return render(request,'generator/about.html')

	