from django.shortcuts import render, redirect
from django.core.mail import send_mail

def home(request): return render(request,"pages/home.html")
def about(request): return render(request,"pages/about.html")
def services(request): return render(request,"pages/services.html")
def projects(request): return render(request,"pages/projects.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        company=request.POST.get("company","")
        service=request.POST.get("service","")
        message=request.POST.get("message","")
        try:
            send_mail(
                f"ZubaLink Website Inquiry - {name}",
                f"Name: {name}\nEmail: {email}\nCompany: {company}\nService: {service}\n\n{message}",
                "zubalink.ltd@gmail.com",
                ["zubalink.ltd@gmail.com"],
                fail_silently=True
            )
        except Exception:
            pass
        return redirect("/contact/")
    return render(request,"pages/contact.html")
