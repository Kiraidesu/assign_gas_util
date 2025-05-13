from django.shortcuts import render, get_object_or_404, redirect

from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'service_requests/thank_you.html')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit.html', {'form': form})

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