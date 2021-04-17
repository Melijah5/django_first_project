from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('show/<int:number>', views.show_by_number),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
    path('redirect', views.redirect_this)
]