from django.shortcuts import render,redirect
from .tasks import send_contact_email
from .models import *

def contact_page(request):
    projects = ProjectData.objects.all()
    skills = Skill.objects.all()
    social = SocialMedia.objects.first()    #6379
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

        send_contact_email.delay(name, email, message)

        return render(request, "home.html", {"success": True})

    return render(request, "home.html",context)



# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")

#           # Celery Background Task

#         return render(request, "success.html")

#     return render(request, "contact.html")

    
    




