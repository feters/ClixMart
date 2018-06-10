from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
	return render_to_response('index.html')

def login(request):
	return render_to_response('login.html')

def change_pass(request):
	return render_to_response('change_pass.html')

def accounts(request):
	return render_to_response('accounts.html')

def add_brand(request):
	return render_to_response('add_brand.html')

def add_cat(request):
	return render_to_response('add_cat.html')

def add_item(request):
	return render_to_response('add_item.html')