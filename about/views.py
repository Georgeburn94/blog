from django.shortcuts import render
from .models import About
from django.http import HttpResponse

# Create your views here.
def about_view(request):
    most_recent_record = About.objects.all().order_by('-updated_on').first()
    return render(request, 'about/about.html', {'most_recent_record': most_recent_record})


    # return render(
    #     request,
    #     "blog/about_me.html",
    #     {"about": about},
    # )