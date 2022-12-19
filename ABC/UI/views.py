from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def loginpage(request):
    if not request.user.is_authenticated:
        return redirect('addcust')
        # return JsonResponse({'status': 'Not yet autheticated'})
