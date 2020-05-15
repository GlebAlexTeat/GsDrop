from django.shortcuts import render
from .models import Profile, Gun, Case
from django.http import HttpResponse
from django.template import loader


def index(request):
   template = loader.get_template('index.html')
   guns = Gun.objects.all()
   context={'guns':guns}
   return HttpResponse(template.render(context,request))

def regestr(request):
   template = loader.get_template('regestr.html')
   users = Profile.objects.all()
   guns = Gun.objects.all()
   context={'users': users, 'guns':guns}
   return HttpResponse(template.render(context,request))
 
# Create your views here.
#    guns_list = Gun.objects.order_by('-title_gun')
    
#         # guns_list += str(i.title_gun) + '\r\n' + str(i.value) + '\r\n\r\n'
     
#     return HttpResponse(guns_list, content_type='text/plain; charset =utf-8')
#     return render(
#         request,
#         'index.html',
#         context={'guns_list':guns_list},
#     )
