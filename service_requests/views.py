from django.shortcuts import render, get_object_or_404, redirect

from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.

def home_view(request):
    #print("Logged in:", request.user.is_authenticated)
    return render(request, 'home.html')

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def user_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user_requests.html', {'requests': requests})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # ← assign user here
            service_request.save()
            return render(request, 'service_requests/thank_you.html')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit.html', {'form': form})


@login_required
def track_request(request):
    request_id = request.GET.get('id')
    result = None
    if request_id:
        result = ServiceRequest.objects.filter(id=request_id).first()
    return render(request, 'service_requests/track.html', {'result': result})

@staff_member_required
def all_requests_view(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'service_requests/all_requests.html', {'requests': requests})

@staff_member_required
def mark_resolved_view(request, request_id):
    req = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        req.status = "Resolved"
        req.resolved_at = timezone.now()
        req.save()
    return redirect('all_requests')