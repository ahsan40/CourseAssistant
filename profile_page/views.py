from django.shortcuts import render
from.models import profile
from.models import add
from.models import comment



# Create your views here.
def Index_2(request):
   from django.core import serializers
   data = serializers.serialize("python",profile.objects.all())
    
   context={
            'data':data,
        }
        
   return render(request,'Index_2.html',context)

def add_content(request):
   
    if request.method == 'POST':
        title = request.POST['title']
        course_code = request.POST['course_code']
        semester = request.POST['semester']
        description = request.POST['description']
        file_name = request.FILES['filename']
      



      
        print(title,course_code,semester,description,file_name.name,file_name.size)
        obj=add()  
        obj.title=title
        obj.course_code=course_code
        obj.semester=semester
        obj.description=description
        obj.file_name=file_name
        obj.save() 


    return render(request,'add_content.html')
def comment_section(request):

     if request.method == 'POST':
        c = request.POST['comment']
       
        obj=comment()  
        obj.comment=c
        obj.save()
        




     return render(request, 'comment_section.html')
   
    


    

