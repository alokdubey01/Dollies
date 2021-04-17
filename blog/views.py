from django.shortcuts import render
from .models import Books,Contact

def home(request):
  book = Books.objects.all()
  return render(request, 'home.html', {'book':book}
  )

def privacy(request):
  return render(request,'privacy.html')
  
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
       # phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email,  content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'contact.html')
def about(request):
  return render(request,'about.html')
    
