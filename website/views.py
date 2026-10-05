from django.shortcuts import render



def home(request):
    context={
        "welcome_title": "Welcome to Our New Website",
        "tagline": "Discover amazing features tailored just for you.",
        
       
        "features": [
            {"title": "harry potter", "description": "Harry Potter is a famous fantasy media franchise centered on a series of seven novels written by British author J.K. Rowling"},
            {"title": "game of thrones ", "description": " Following the death of the King, several noble houses—primarily the Starks, Lannisters, Baratheons, and Targaryens—engage in a brutal web of political intrigue, civil war, and psychological scheming to claim total rule over the Seven Kingdoms."},
            {"title": "vikings", "description": " The first half of the series centers on Ragnar Lothbrok (played by Travis Fimmel), a visionary farmer and warrior who frustrates his local chieftain by daring to sail west into uncharted waters. Alongside his shield-maiden wife Lagertha and his eccentric shipbuilder friend Floki, Ragnar orchestrates the first Norse raids on England and France, eventually rising to become the King of the Viking tribes."},
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
