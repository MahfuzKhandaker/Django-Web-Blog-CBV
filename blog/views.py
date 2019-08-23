from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from blog.forms import CommentForm
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
) 
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from blog.models import Post, Comment, Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PageContextMixin(object):
    page_title = None

    def get_context_data(self, **kwargs):
        context = super(PageContextMixin, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context
        

class Home(PageContextMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = '-created_on'
    paginate_by = 3
    page_title = 'Home'

@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self, request, *args, **kwargs):
        view = Home.as_view(
            template_name = 'blog/dashboard_admin.html'
        )
        return view(request, *args, *kwargs)


# class PostDisplay(DetailView):
#     model = Post

#     def get_object(self):
#         object = super(PostDisplay, self).get_object()
#         object.view_count += 1
#         object.save()
#         return object

#     def get_context_data(self, **kwargs):
#         context = super(PostDisplay, self).get_context_data(**kwargs)
#         context['comments'] = Comment.objects.filter(post=self.get_object())
#         context['form'] = CommentForm()
#         return context

class PostDisplay(PageContextMixin, SingleObjectMixin, View):
    model = Post
    page_title = 'Detail'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.view_count += 1
        self.object.save()
        post = self.get_context_data(object=self.object)
        return render(request, 'blog/post_detail.html', post)

    def get_context_data(self, **kwargs):
        context = super(PostDisplay, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        context['form'] = CommentForm()
        return context


class PostComment(FormView):
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        form.instance.comment_by = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.post = post
        form.save()
        return super(PostComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'] })


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    fields = ('title', 'category', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(PostCreate, self).form_valid(form)
        

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    fields = ('title', 'category', 'content')


@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard')


class PostCategory(ListView):
    model = Post
    template_name = 'blog/post_category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


    
