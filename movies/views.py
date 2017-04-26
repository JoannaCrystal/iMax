from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    """ home page """
    return render(request, 'movies/index.html')

@login_required
def account_redirect(request):
    """redirect url"""
    return redirect('account_landing', pk=request.user.pk, name=request.user.username)

@login_required
def profile(request, pk, name):
    """ profile page """
    # return HttpResponse("Welcome %s." % name)
    context = {'name': name}
    return render(request, 'movies/profile.html', context)







