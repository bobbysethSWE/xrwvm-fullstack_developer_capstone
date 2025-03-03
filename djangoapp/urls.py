# Uncomment the imports before you add the code
# from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views  # Import your views module

app_name = 'djangoapp' 
urlpatterns = [
    

    # path('admin/', admin.site.urls),
    # path('djangoapp/', include('djangoapp.urls')),
    path('about/', TemplateView.as_view(template_name="About.html")),
    # # path for registration

    # path for login
    # path(route='login', view=views.login_user, name='login'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
