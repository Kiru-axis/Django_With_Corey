from django.shortcuts import render

# Create your views here.

# dummy data
posts = [
    {"title": "Hacker 101",
    "author": "John Obala",
    "content": "There is more than what you see",
    "date_posted": "January 23 2021"
    },
    {"title": "Black is power",
    "author": "Mercy Cheyech",
    "content": "just explore deeper",
    "date_posted": "February 2 2021"
    },
    {"title": "Get that power",
    "author": "Grace Mwihaki",
    "content": "Step by step through successful gain of power",
    "date_posted": "June 13 2021"
    }
]

# view functions
def home(request):
    context = {
        "posts":posts,
        "title":"Home Page"
        
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html")