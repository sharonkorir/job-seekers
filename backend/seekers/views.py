from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Comment, User, Rate, Pitch, Resume
from .forms import ResumeForm, RateForm, PitchForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
  resumes = Resume.objects.all()
  context = {
    'resumes':resumes,
  }
  return render(request,'index.html', context)

def pitch(request):
  pitches = Pitch.objects.all()
  context = {
    'pitches':pitches,
  }
  return render(request,'pitch/pitches.html', context)

def profile(request):
    user = request.user
    resume = Resume.objects.filter(profile=user)
    pitch = Pitch.objects.filter(profile=user)
    return render(request, 'profile.html', {'user':user, 'resume':resume, 'pitch':pitch})

def cv_details(request, pk):
    resume = Resume.objects.filter(pk=pk)
    rates = Rate.get_rate_count(pk)
    if rates > 0:
        
        averages = Rate.find_sum(pk)
        conciseness = averages[0]
        professionalism = averages[1]
        flow = averages[2]
        average = averages[3] 
        context = {
          'resume': resume,
          'conciseness': conciseness,
          'professionalism': professionalism,
          'flow': flow,
          'average': average,
        }
    else:
        context = {
          'resume':resume,

        }

    return render(request, 'resumes/cv_detail.html', context)

@login_required()
def upload_cv(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ResumeForm()

    return render(request, 'resumes/upload_cv.html', {'form':form})

@login_required()
def rate_cv(request, pk):
    resume = Resume.objects.get(id=pk)
    user = request.user

    if request.method == 'POST':
        form = RateForm(request.POST)
        print('test form',form)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.profile = user
            rate.cv = resume
            rate.save()
            print('test form save' ,rate)
            
            return HttpResponseRedirect(reverse('cv_details', args=pk))
            
    else:
        form = RateForm()
        print('request is not POST')

    context = {
      'form':form,
      'resume':resume
    }
    print(user, resume)
    return render(request, 'resumes/rate_cv.html', context)

@login_required()
def submit_pitch(request):
    form = PitchForm()
    if request.method == 'POST':
        form = PitchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pitch')
    else:
        form = PitchForm()

    return render(request, 'pitch/submit_pitch.html', {'form':form})

def pitch_details(request, pk):
    pitch = Pitch.objects.filter(pk=pk)
    comments = Comment.objects.filter(pitch=pitch)
    
    context = {
      'pitch':pitch,
      'comments':comments,
    }

    return render(request, 'pitch/pitch_detail.html', context)

@login_required()
def comment(request, pk):
    pitch = Pitch.objects.get(id=pk)
    user = request.user

    if request.method == 'POST':
        form = CommentForm(request.POST)
        print('test form',form)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = user
            comment.pitch = pitch
            comment.save()
            print('test form save' ,comment)
            
            return HttpResponseRedirect(reverse('pitch_details', args=pk))
            
    else:
        form = CommentForm()
        print('request is not POST')

    context = {
      'form':form,
      'pitch':pitch
    }
    print(user, pitch)
    return render(request, 'pitch/comment.html', context)


