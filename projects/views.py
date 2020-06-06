from .Calls import Calls
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.db import IntegrityError
from auth.models import appusers
from .models import projects
from .models import user
from django.template.response import TemplateResponse

# Create your views here.
def createproject(request):
    if request.method == 'POST':
        if request.POST.get('jobtitle') and request.POST.get('privacytype') and  request.POST.get('job-type') and request.POST.get('payment-type') and request.POST.get('category-type')  and  request.POST.get('jobdescription') :
            Projects = projects()
            Projects.jobtitle = request.POST.get('jobtitle')
            Projects.jobtype = request.POST.get('job-type')
            Projects.paymentmethod = request.POST.get('payment-type')
            Projects.jobdescription = request.POST.get('jobdescription')
            Projects.category= request.POST.get('category-type')
            Projects.privacy = request.POST.get('privacytype')
            Projects.createdby =request.session.get("username")
            Projects.save()

            return redirect('/')
    else:
        return render(request, 'CreateProject.html')


# profile view (it has to get the search data to pass dynamically to html file)
def profilepage(request):  # (request,username):
    callobject = Calls()
    user1 = callobject.profilecall(request)
    #showing project created by client
    #myProjects = projects.objects.filter(createdby=request.session.get("username"))
    context = {'user1':user1 }
    return render(request, "ProfilePage.html", context)



def searchproject(request):
    arguments = {}
    arguments['mnm'] = ''
    if request.method == 'POST':
        if "SearchP" in request.POST:
            if  request.POST.get('projecttext'):
                textinjob = request.POST.get('projecttext')
                mainCategory = request.POST.get('projectcategory')
                criterion1 = Q(jobtitle__exact=textinjob)
                criterion2 = Q(jobtype__icontains=mainCategory)
                if request.session.get('username'):
                    allProjects = projects.objects.filter(criterion1 | criterion2 )
                    return render(request, 'ProjectListing.html', {'Projects': allProjects})  # contains the text
                else:
                    publicProjects = projects.objects.filter(Q(privacy="Public") & criterion1)
                    return render(request, 'ProjectListing.html', {'Projects': publicProjects})  # contains the text
            else:
                arguments['mnm'] = "! Place at least one keyword !"
                return render(request, 'MainPage.html', arguments)

        elif "SearchU" in request.POST:
            if request.POST.get('username'):
                user = request.POST.get('username')
                cat = request.POST.get('usertype')
                return render(request, 'ProjectListing.html',{'Projects':Projects})
            else:
                return render(request, 'MainPage.html', {'mnm': mnm})
        elif "profile" in request.POST:
            if request.session.get('username'):
                callobject = Calls()
                user1 = callobject.profilecall(request)
                return render(request, "ProfilePage.html", {'user1': user1} )
            else:
                arguments['mnm'] = "! You have to log in to see your profile click the register buttom !"
                return render(request, 'MainPage.html', arguments)
        else:
            return HttpResponse("<p> No input </p> ")
    #Projects in {} refer to html / data passed to html
    #Projects = projects.objects.filter(jobtitle=jobtitle)
    #context = {'Projects':Projects}
    else:
        if request.session.get('username'):
            allprojects = projects.objects.all()[:4]
            return render(request, 'MainPage.html', {'allprojects': allprojects})
        else:
            # showing only public projects
            publicprojects = projects.objects.filter(privacy="Public")[:4]
            return render(request, 'MainPage.html', {'allprojects': publicprojects})



#projectlisting
#def toprojectpage(request):
        #jobtitle = request.POST.get('jobtitle')
        #Projects = projects.objects.filter(jobtitle=jobtitle)
        #return render(request, 'ProjectPage.html' , {'Projects':Projects})
    #Projects in {} refer to html / data passed to html
    #Projects = projects.objects.filter(jobtitle=jobtitle)
    #context = {'Projects':Projects}


def projectdetails(request,pk):
    #pk is called in the url path
    Projects= projects.objects.get(id=pk)
    context = {'Projects':Projects}
    return render(request, 'ProjectPage.html',context)


def myprojects(request):
    if request.session.get('username'):
        #check if client or developer
        if request.session['idiotita'] == 'client':
            myProjects = projects.objects.filter(createdby=request.session.get("username"))
            return render(request, 'MyProjects.html', {'myProjects': myProjects})
        else:
            return HttpResponse("You are not a client")
    else:
        return HttpResponse("You are not logged in")



