from auth.models import appusers
from .models import *
from django.db.models import Q

class Calls():

    """docstring for Calls."""

    def __init__(self):
        pass

    def profilecall(self, request):
        user1 = appusers()
        result = appusers.objects.filter(username=request.session.get("username"))

        user1.user = result.values_list('username', flat=True)[0]
        user1.username = result.values_list('fullname', flat=True)[0]
        user1.location = result.values_list('location', flat=True)[0]
        user1.birthday = result.values_list('birthday', flat=True)[0]
        user1.gmail = result.values_list('email', flat=True)[0]
        user1.twlink = 'test'
        user1.fblink = 'test'
        user1.gitlink = 'test'


        if request.session.get('idiotita') == 'developer':
            result1 = developerinfo.objects.filter(username=request.session.get("username"))
            try:

                user1.info1 = result1.values_list('github', flat=True)[0]
                user1.info2 = result1.values_list('cv', flat=True)[0]
                user1.info3 = result1.values_list('language', flat=True)[0]
                user1.profile_pic = 'test'# result1.values_list('profile_pic', flat=True)
                user1.location = result1.values_list('location', flat=True)[0]

            except IndexError as e:
                user1.info1 = 'not available'
                user1.info2 = 'not available'
                user1.info3 = 'not available'
                user1.location1 = result.values_list('location', flat=True)[0]


        if request.session.get('idiotita') == 'client':

            result2 = customerinfo.objects.filter(username=request.session.get("username"))
            try:
                user1.info1 = result2.values_list('linkedin', flat=True)[0]
                user1.info2 = result2.values_list('disc', flat=True)[0]
                user1.info3 = " "
                user1.profile_pic = 'not available'# result2.get('profile_pic', flat=True)[0]
                user1.location = result2.values_list('location', flat=True)[0]

            except IndexError as e:
                user1.info1 = 'not available'
                user1.info2 = 'not available'
                user1.info3 = 'not available'
                user1.location = result.values_list('location', flat=True)[0]





        return user1

    def searchP(self,request):
        textinjob = request.POST.get('projecttext')
        mainCategory = request.POST.get('projectcategory')
        details = request.POST.get('detail')
        criterion1 = Q(jobtitle__icontains=textinjob)
        criterion2 = Q(jobtype__iexact=mainCategory)
        criterion3 = Q(jobdescription__exact=details)
        if request.session.get('username'):
            if  "No category" == mainCategory:
                allProjects = projects.objects.filter( (criterion1 | criterion3) )
            else:
                allProjects = projects.objects.filter( (criterion1 | criterion3) &  criterion2 )
            return allProjects
        else:
            publicProjects = projects.objects.filter(Q(privacy="Public") & criterion1)
            return publicProjects

    def searchU(self, request):
        criterion1 = Q(username__icontains=request.POST.get('username'))
        criterion2 = Q(idiotita__iexact=request.POST.get('usertype'))
        criterion3 = request.POST.get('nprojects')
        criterion4 = Q(isCopletedbyClient=True)
        criterion5 = Q(offerby__exact=request.POST.get('username'))
        criterion6 = Q(rating__iexact=request.POST.get('rating'))
        username = request.session.get('username')

        ######
        if "SearchUA" in request.POST:
            doneprojects = projects.objects.filter( criterion4 ) #completed projects
            done_dev = []
            show_dev = [] #dev to search
            if criterion3:
                for i in doneprojects:
                    #done_dev.append(i.tagdev)
                    criterion5 = Q(offerby__exact=i.offerby)
                    numprojects = projects.objects.filter( criterion4 & criterion5).count() # number of projects from username
                    if numprojects >= int(criterion3):
                        show_dev.append(i.offerby)
                criterionmulusername = Q(username__in=show_dev)
                allUsers = appusers.objects.filter( criterionmulusername | criterion6 ) #Users with username Advance search
            else:
                allUsers = appusers.objects.filter( criterion6 ) #Users with username Advance search

            ################
            #criterion4 = Q(idiotita__exact=request.POST.get('rating')) search on appusers
        else:
            allUsers = appusers.objects.filter(criterion1 & criterion2 ) #Users with username simple search


        return allUsers
