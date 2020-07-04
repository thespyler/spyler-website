from django.shortcuts import render

def main(request):
	return render(request, 'main.html')
# Create your views here.

def c(request):
	return render(request, 'c.html')

def django(request):
	return render(request, 'django.html')

def flask(request):
		return render(request, 'flask.html')

def matplotlib(request):
	return render(request, 'matplotlib.html')

def signup(request):
	return render(request, 'signup.html')

