from django.shortcuts import render,redirect
from .models import *

def contact_page(request):
    projects = ProjectData.objects.all()
    skills = Skill.objects.all()
    social = SocialMedia.objects.first()
    context = {
        "projects": projects,
        "skills": skills,
        "social": social
    }
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message 
        )

        return render(request, "home.html", {"success": True})

    return render(request, "home.html",context)


    
    




