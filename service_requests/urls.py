from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),
    path('all/', views.all_requests_view, name='all_requests'),
    path('resolve/<int:request_id>/', views.mark_resolved_view, name='mark_resolved'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my-requests/', views.user_requests, name='user_requests'),
    path('signup/', views.signup_view, name='signup'),

]
