from django.shortcuts import render
from .models import Featured_projects,Research

# Create your views here.
def home(request):


    # context = {
    #     'featured_projects':F_projects,
    # }
    return render(request,"home.html")


def research(request):
    ieee_obj = Research.objects.filter(publication="IEEE")
    springer_obj = Research.objects.filter(publication="Springer")
    Patent = Research.objects.filter(research_type='P')
    Book_Featured = Research.objects.filter(research_type='B')

    context = {
        'ieee' : ieee_obj,
        'springer':springer_obj,
        'patents':Patent,
        'book_featured':Book_Featured,
    }

    return render(request,"research.html",context)

# def contact(request):
#     return render(request,"contact.html")

# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = 'New Contact Form Submission'
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            sender_email = settings.DEFAULT_FROM_EMAIL
            recipient_email = 'chawlamohit45@gmail.com'  # Your email address

            send_mail(subject, body, sender_email, [recipient_email])
            
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})




# API ENDPOINTS

from django.http import JsonResponse
from mohit.models import Projects,Featured_projects

def projects_api_view(request):
    projects = Projects.objects.all()
    domain_projects = {}

    # Filter and group projects by domain
    for project in projects:
        domain = project.Domain
        if domain not in domain_projects:
            domain_projects[domain] = []
        
        domain_projects[domain].append({
            'name': project.name,
            'url': project.link
        })

    # Create a list of domain-wise projects
    project_data = []
    for domain, projects in domain_projects.items():
        project_data.append({
            'domain': domain,
            'count': len(projects),
            'projects': projects
        })

    return JsonResponse(project_data, safe=False)


from random import choice
from django.http import JsonResponse
from .models import Featured_projects
import re

def featured_projects_api(request):
    try:
        featured_project = Featured_projects.objects.select_related('Featured_project')
        
        if featured_project:
            random_project = choice(featured_project)
            project = random_project.Featured_project
            # Extract the first 10 words from the description
            description_words = re.findall(r'\b\w+\b', project.description)[:10]
            description = ' '.join(description_words)

            tags = project.tags.split(',')[:2]
            
            featured_project_data = {
                'name': project.name,
                'description': description,
                'tags':tags,
                # Add more fields as needed
            }
            
            return JsonResponse(featured_project_data, safe=False)
        
        return JsonResponse({}, status=404)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
