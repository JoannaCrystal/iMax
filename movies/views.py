from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .models import Profile
import urllib

# Create your views here.
def index(request):
    """ home page """
    return render(request, 'movies/index.html')

@login_required
def account_redirect(request):
    """redirect url"""
    return redirect('account_landing', pk=request.user.pk, name=request.user.username)

@login_required
def redirect_to_third_party_api(request):
    """redirect to our app"""
    # print("hi:"+str(request.user.pk))
    profile_user = Profile.objects.get(user=request.user)
    # print("pro:"+profile_user.phone_number)
    context = {'name': request.user.username, 'phone_number': profile_user.phone_number}
    # return redirect('http://www.google.com')
    return render(request, 'movies/confirm.html', context)

# @login_required
# def redirect_to_third_party_api(request):
#     """redirect to our app"""
#     url = "http://ec2-52-14-223-254.us-east-2.compute.amazonaws.com/"
#     values = {'username':request.user.username}
#     data = urllib.parse.urlencode(values).encode("utf-8")
#     req = urllib.request.Request(url, data)
#     response = urllib.request.urlopen(req)
#     result = response.read()
#     print(result)

@login_required
def profile(request, pk, name):
    """ profile page """
    # return HttpResponse("Welcome %s." % name)
    context = {'name': name}
    return render(request, 'movies/profile.html', context)







