from django.shortcuts import render



def home(request):
    context={
        "welcome_title": "Welcome to Our New Website",
        "tagline": "Discover amazing features tailored just for you.",
        
       
        "features": [
            {"title": "Easy Coding", "description": "Django makes web development fast and fun."},
            {"title": "Clean Templates", "description": "Dynamic data prints safely to your HTML page."},
            {"title": "Instant Updates", "description": "Change it here in Python, and it updates instantly."},
        ]}
    return render(request,'home.html',context)


def contact(request):
    context={ "title": "Contact Us",
        "email": "ganesh@mycompany.com",
        "phone": "9869419270",
        "available_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "urgent_notice": False
       
        }
    return render(request,'contact.html',context)
def about(request):
    context={
       "title": "About Our Company",
        "address": "jarankhu, nepaltar",
        
    
        "services": ["Web Design", "SEO Optimization", "App Development"],
        
       
        "is_open_now": True,
        
      
        "founded_year": 2015,
        }
    return render(request,'about.html',context)


# we can change value in view dont need to vchange in inside html
# use bootstrap
#should go in title of index
#keys passed in .html    # return render(request,'contact.html')
# Create your views here.
