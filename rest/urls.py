from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('v1/calendar/init/', views.google_calendar_init_view, name='google_permission'),
    path('v1/calendar/redirect/', csrf_exempt(views.google_calendar_redirect_view), name='google_redirect')
]