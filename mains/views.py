from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request, 'mains/homepage.html')


def about(request):
	return render(request, 'mains/about.html')

def store(request):
	return render(request, 'mains/store.html')