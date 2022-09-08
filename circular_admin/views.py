from django.shortcuts import render
from .forms import NewCircularForm, JobPostForm, MemorandumForm
from .models import NewCircular, JobPost, Memorandum
from registration_app.models import Account

# Create your views here.

def new_memorandum_view(request):
  memo_form = MemorandumForm()

  if request.method == 'POST':
    memo_form = MemorandumForm(request.POST)
    if memo_form.is_valid():
      memo_form.save()
    else:
      print(memo_form.errors)

  data = {
    'memo_form':memo_form,
  }

  return render(request, 'circular_admin/memorandum_form.html', context=data)


def new_job_post_view(request):
  job_post_form = JobPostForm()

  if request.method == 'POST':
    job_post_form = JobPostForm(request.POST)

    if job_post_form.is_valid():
      job_post_form.save() 

  data = {
    'job_post_form':job_post_form,
  }

  return render(request, 'circular_admin/job_post_form.html', context=data)

def new_circular_view(request):
  
  circular_form = NewCircularForm()

  if request.method == 'POST':

    circular_form = NewCircularForm(request.POST)

    if circular_form.is_valid():
      circular_model = NewCircular()
      user = request.user
      user.save()
      # obj = NewCircular.objects.create(user=user)
      # circular_form = NewCircular(request.POST, instance=obj)
      # circular_form.save()

      circular_model.user = request.user

      circular_model.memorandum_with_date = circular_form.cleaned_data['memorandum_with_date']
    
      circular_model.post = circular_form.cleaned_data['post']

      # NewCircular.save()
      # circular_form.save()
      circular_model.save()

    else:
      print(circular_form.errors)

  data = {
    'circular_form':circular_form,
  }

  return render(request, 'circular_admin/new_circular_form.html', context=data)
