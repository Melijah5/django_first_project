from django.shortcuts import render, HttpResponse , HttpResponseRedirect

def index(request):
    return HttpResponse('/')

def new(request):
    return HttpResponse("<h1>New form to create a new blog</h1>")

def create(request):
    return HttpResponseRedirect('/')  
    # return HttpResponse("<h1>create new blogger</h1>")

def show_by_number(request, number):
    print(f"The requested number is {number}")
    return HttpResponse(f"blog number: {number}")

def edit(request, number):
    print(f"The requested number is {number}")
    return HttpResponse(f"Edit blog number: {number}")

def destroy(request, number):
    print(f"The requested number is {number}")
    return HttpResponseRedirect('/')  
    # return HttpResponse(f"Are you sure to delete blog number: {number}")

def redirect_this(request):
    print(f"you hit the redirect url")
    return HttpResponseRedirect('/')   