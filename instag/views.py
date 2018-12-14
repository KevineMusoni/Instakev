from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import InstaLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect

def welcome(request):
    return render(request, 'base.html')

@login_required(login_url='/accounts/login/')
def user(request, user_id):
    try:
        article = User.objects.get(id = user_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"registration/views.html", {"user":user})

def insta(request):
  if request.method == 'POST':
        form = InstaLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InstaLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('insta')
    else:
        form = InstaLetterForm()
    return render(request, 'index.html')

