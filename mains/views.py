from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request, 'homepage.html')


def about(request):
	return render(request, 'about.html')

def store(request):
	return render(request, 'store.html')