from django.shortcuts import render
from .models import content, Content_request


# Create your views here.


def home(request):
    #fetch data from database

    from django.core import serializers
    contentss=serializers.serialize("python",content.objects.all()) 

    context = {
        
        'c': contentss,
    }
    


    return render(request, 'homepage.html',context)



def request_content(request):
    #save data in  database
    if request.method=="POST" :
        title=request.POST['title']
        code=request.POST['course_code']
        semester=request.POST['semester']
        description=request.POST['description']
       

        

        if len(title)!=0 and len(code)!=0  and len(semester)!=0  and len(description)!=0 :
          obj=Content_request()  
          obj.course_name=title
          obj.course_code=code
          obj.semester=semester
          obj.description=description

          obj.save() 

       
   
    


    return render(request, 'request_content.html')





def messages(request):
    return render(request, 'messages.html')


def chat(request):
    return render(request, 'chat.html')
