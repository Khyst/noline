from django.shortcuts import render

# Create your views here.
def login(requests):
    return render(requests, 'login.html')

def join(requests):
    return render(requests, 'join.html')

def logout(requests):
    
    pass
