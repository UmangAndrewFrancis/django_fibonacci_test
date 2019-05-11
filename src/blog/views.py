from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost
from .helper import Fibonacci
import time

@staff_member_required
def blog_post_create_view(request):
    input_value = None
    fib_val = None
    time_taken = None
    start_time = time.time()
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        input_value = obj.content
        print(input_value)
        fib_val = Fibonacci(input_value)
        form = BlogPostModelForm()
        time_taken = time.time() - start_time
    template_name = 'form.html'
    context = {'form': form, 'content_display': fib_val, 'time_taken': time_taken}
    return render(request, template_name, context)


