from django.shortcuts import render
from registration_app.forms import AccountForm, ApplicantRegisterForm, AddCircularForm, ApplicantDocumentForm
from django.contrib.auth.models import User, Group

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from registration_app.models import AddCircular, ApplicantRegister, Account, ApplicantDocument

from django.utils.encoding import force_bytes, force_text

from django.contrib.sites.shortcuts import get_current_site  
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.core.mail import EmailMessage  
from .token import account_activation_token  
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

# Create your views here.

Account = get_user_model()

def activate(request, uidb64, token):  
    # User = get_user_model()  
    # print('User', User)
    print(request.user)
    try:  
      uid = force_text(urlsafe_base64_decode(uidb64))  
      user = Account.objects.get(pk=uid)  
      print(uid, user)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):  
      user = None  
    if user is not None and account_activation_token.check_token(user, token):  
      user.is_active = True  
      user.save()  
      group = Group.objects.get(name='applicant-permission')
      user.groups.add(group)

      print(group, user)

      return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
      return HttpResponse('Activation link is invalid!')  

def login_page(request):
  return render(request, 'registration_app/login.html', context={})

def user_login(request):
  if request.method == 'POST':
    email = request.POST.get('email') # input field ee j name dici se onusare get korteci value
    password = request.POST.get('password')

    print(email, password)
    user = authenticate(username=email, password=password)
    print(user)
    if user:
      if user.is_active:
        login(request, user)

        # To change the urlpatterns we are using this method
        return HttpResponseRedirect(reverse('registration_app:index'))

        # if we return using render function then urlpatterns does not change that's why we need to use previous method
        # return render(request, 'registration_app/index.html', context={})

        # this method also does not change urlpatterns
        # return index(request)
      else:
        return HttpResponse('Account is not active')
    else:
      return HttpResponse('Log In details are wrong')
  
  else:
    # return render(request, 'registration_app/login.html', context={})
    return HttpResponseRedirect(reverse('registration_app:login'))

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('registration_app:index'))

def index(request):
  dict = {}

  if request.user.is_authenticated:
    current_user = request.user
    print(current_user.id)
    # print(current_user.username)
    user_id = current_user.id
    user_basic_info = Account.objects.get(pk=user_id)
    print('id', user_id)
    # user_more_info = UserInfo.objects.get(pk=user_id)
    dict = {
      'user_basic_info': user_basic_info,
      # 'user_more_info': user_more_info
    }
  return render(request, 'registration_app/index.html', context=dict)


def register(request):

  registered = False

  if request.method == 'POST':
    user_form = AccountForm(data=request.POST)
    user_info_form = ApplicantRegisterForm(data=request.POST)

    if user_form.is_valid() and user_info_form.is_valid():
      user = user_form.save(commit=False)
      user.is_applicant=True
      user.set_password(user.password) # password encrypt
      user.save()

      if user_info_form.is_valid():
        user_info = user_info_form.save(commit=False) # False dile DB save korbe na, user_info te hold kore rakbe
        
        user_info.user = user # user_info te user namer field take relate kortece

        if 'profile_pic' in request.FILES:
          user_info.profile_pic = request.FILES['profile_pic']
        
        user_info.save()
        registered = True
      else:
        print('Ekane', user_info_form.errors)

      current_site_info = get_current_site(request)  
      mail_subject = 'The Activation link has been sent to your email address'  
      message = render_to_string('registration_app/acc_active_email.html', {  
          'user': user,  
          'domain': current_site_info.domain,  
          'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
          'token':account_activation_token.make_token(user),  
      })  
      to_email = user_form.cleaned_data.get('email')  
      email = EmailMessage(  
                  mail_subject, message, to=[to_email]  
      )  
      print('email sent')
      email.send()  
      
      return HttpResponse('Please proceed confirm your email address to complete the registration')
    else:
      print('ERrors', user_form.errors, user_info_form.errors)

  else:
    user_form = AccountForm()
    user_info_form = ApplicantRegisterForm()

  dict = {
    'user_form': user_form, 
    'user_info_form': user_info_form,
    'registered': registered
  } 

  return render(request, 'registration_app/register.html', context=dict)

@login_required
@permission_required('registration_app.add_account')
def add_circular_admin(request):

  circular = AccountForm()

  if request.method == 'POST':
    circular = AccountForm(data=request.POST)
    
    if circular.is_valid():
      print('valid data', circular)
      user = circular.save()

      user.set_password(user.password)
      user.is_circular_admin = True
      user.save()

      group = Group.objects.get(name='circular-permission')
      user.groups.add(group)

      return HttpResponse("Added circular admin")
    else:
      print("Errors in data", AccountForm.errors)

  data = {
    'circular': circular,
  }

  return render(request, 'registration_app/add_circular_admin.html', context=data)

@login_required
@permission_required('registration_app.add_addcircular')
def add_circular_form(request):
  circular_form = AddCircularForm()

  if request.method == 'POST':
    user = request.user
    user.save()
    obj = AddCircular.objects.create(user=user)
    circular_form = AddCircularForm(request.POST, instance=obj)
    print(request.user)
    if circular_form.is_valid():
      circular_form.save()
    else:
      print(circular_form.errors)

  data = {
    'circular_form': circular_form,
  }

  return render(request, 'registration_app/add_circular_form.html', context=data)


@login_required
@permission_required('registration_app.add_applicantdocument')
def add_applicant_document(request):
  
  applicant_document = ApplicantDocumentForm()

  if request.method == 'POST':
    print('applicant', request.user)
    user = request.user
    user.save()
    obj = ApplicantDocument.objects.create(applicant=user)
    applicant_document = ApplicantDocumentForm(request.POST, instance=obj)

    if applicant_document.is_valid():
      applicant_document.save()
    else:
      print(applicant_document.errors)

  data = {
    'applicant_document': applicant_document,
  }

  return render(request, 'registration_app/applicant_document.html', context=data)