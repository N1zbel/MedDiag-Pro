from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Review
from .forms import ReviewForm


def about_us_view(request):
    reviews = Review.objects.all()
    form = ReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.created_at = timezone.now()
        review.save()
        return redirect('about_us:about_us_view')

    return render(request, 'about_us/about_us.html', {'reviews': reviews, 'form': form})
