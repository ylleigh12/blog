from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import post_form, update_post_form, comment_form
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})
class home_view(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-post_date']
    ordering = ['-id']

class post_detail_view(DetailView):
    model = Post
    template_name = 'post_details.html'

class add_post_view(CreateView):
    model = Post
    form_class = post_form
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class update_post_view(UpdateView):
    model = Post
    form_class = update_post_form
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class delete_post_view(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class add_comment_view(CreateView):
    model = Comment
    form_class = comment_form
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
        
    # success_url = reverse_lazy('home')
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})

class delete_comment_view(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        # post = Post.objects.get(pk=self.object.post.pk)
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
