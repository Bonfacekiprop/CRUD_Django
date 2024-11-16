from django.shortcuts import render,redirect
# import models from sub_app
from sub_app.models import Speaker


# Create your views here.

def home(request):  
    return render(request, 'starter-page.html')
def starter(request):   
    return render(request, 'index.html')
def speaker(request):   
    return render(request, 'speaker-details.html')
def addspeaker (request): 
    if request.method == "POST":
        spker_name = request.POST['spker_name']
        speaker_qt = request.POST['speaker_qt']
        spker_desc = request.POST['spker_desc']
        spker_img = request.FILES['spker_img']
        
        speaker = Speaker(
            spker_name = spker_name,
            speaker_qt = speaker_qt,
            spker_desc = spker_desc,
            spker_img = spker_img,
            
        )
        speaker.save()
        return redirect('/')
         
    return render(request,'add_speaker.html')
def viewspeaker(request):
    speaker = Speaker.objects.all()
    return render(request,'index.html',{"speaker": speaker})