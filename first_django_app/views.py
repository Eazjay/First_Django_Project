from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return redirect("/blogs")

def json_response(request):
    comment =  {
                    'title': 'My first blog', 
                    'comments': 'I love to code but sometimes I feel like quiting lol!!!'
                }
    return JsonResponse(comment)