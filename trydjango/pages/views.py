from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "page/home.html", {}) # string of HTML code return # HttpResponse("<h1>Hello World</h1>")


def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>") # string of HTML code
	return render(request, "page/contact.html", {})

def about_view(request, *args, **kwargs):
    
    my_context = {
        "my_text"   : "This is about us",
        "my_number" : 123,
        "my_list"   : [123, 4242, 12313, "abc"]
    }

    return render(request, "page/about.html", my_context)


def social_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Social Page</h1>") # string of HTML code
	return render(request, "page/social.html", {})