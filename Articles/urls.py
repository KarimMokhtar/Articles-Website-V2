from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Articles'
urlpatterns = [
    # Post Urls
    path('', views.Pindex, name = 'Pindex'),
    path('<int:post_id>',views.Pshow, name = 'Pshow'),
    path('createPost',views.Pcreate, name = 'Pcreate'),
    path('storePost',views.Pstore, name = 'Pstore'),
    path('<int:post_id>/updatePost',views.Pupdate, name = 'Pupdate'),
    path('<int:post_id>/editPost',views.Pedit, name = 'Pedit'),
    path('<int:post_id>/deletePost',views.Pdelete, name = 'Pdelete'),
    
    
    # comment Urls
    path('comment/<int:post_id>', views.Cstore, name = 'Cstore'),
    
    
    # replies Urls
    path('reply/<int:comment_id>', views.Rstore, name = 'Rstore'),
]