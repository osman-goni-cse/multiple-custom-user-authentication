from django.urls import path
from circular_admin import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'circular_admin' 

urlpatterns = [
    path('newCircular/', views.new_circular_view , name='new-circular'),
    path('newMemorandum/', views.new_memorandum_view , name='new-memorandum'),
    path('newJobPost/', views.new_job_post_view , name='new-job-post'),
]
