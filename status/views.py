from django.shortcuts import render, redirect
from .models import Status
from .forms import StatusForm, StatusReviewForm
from django.contrib import messages

# Create your views here.

def statuses(request):
    statuss = Status.objects.all()

    form = StatusForm()
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.owner = request.user.profile
            status.save()
            messages.success(request, 'Your status was successfully posted')
            return redirect('statuses')

    for status in statuss:
        status.getUpVote
        print(status.upvotes)

    context = {
        'statuss' : statuss,
        'form' : form
    }

    return render(request, 'status/statuss.html', context)

