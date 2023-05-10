from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """View to return index page"""
    return render(request, 'bag/bag.html')