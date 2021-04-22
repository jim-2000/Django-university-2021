'''



'''

from django.urls import path
from . import views
 
urlpatterns = [
    # path('',StudentAccount.as_view(), name='Student-Register'),
    path('login/',views.getlogin, name='Login'),
    path('login/',views.getlogOut, name='Logout'),
    # path('teacher/',TeachertAccount.as_view(), name='JOIN'),
]