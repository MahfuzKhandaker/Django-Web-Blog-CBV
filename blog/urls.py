from django.urls import path
from blog.views import(
    Home,
    PostDetailView,
    PostCategory,
    PostCreate,
    PostUpdate,
    PostDelete,
    Dashboard
) 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/category/<int:pk>/', PostCategory.as_view(), name= 'post-by-category'),
    path('post/create/', PostCreate.as_view(), name= 'post-create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name= 'post-update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name= 'post-delete')
]