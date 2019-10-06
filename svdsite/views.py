from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'svdsite/index.html', {})
def about(request):
    return render(request, 'svdsite/about.html', {})
def items(request):
    return render(request, 'svdsite/items.html', {})
def portfolio(request):
    return render(request, 'svdsite/portfolio.html', {})
def contact(request):
    return render(request, 'svdsite/contact.html', {})