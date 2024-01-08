from django.urls import path
from bankingapp.views import user_success,search_accounts,user_dashboard,create_account,userp,success,user_login,user_reg,logout,calculate_interest,cashier_mainpage,cashier_login,cashier_register,login,register,index,otp,create_transaction,display,withdrawal,deposit,cash,report
from django.conf import settings
from django.conf.urls.static import static

app_name='bankingapp'
urlpatterns =[
    path('cashierhome/',cashier_mainpage,name='cashier_mainpage'),
    path('',index,name='index'),
    path('l/',login,name='login'),
    path('logout',logout,name="logout"),
    path('r/',register,name='register'),
    path('otp/<str:otp>/<str:username>/<str:password>/<str:email>/', otp, name='otp'),
    path('create/',create_transaction,name="create_transaction"),
    path('display/',display,name='display'),
    path('cash/',cash,name='cash'),
    path('report/',report,name='report'),
    path('w/',withdrawal,name='withdrawal'),
    path('create-account/', create_account, name='create_account'),
    path('d/',deposit,name='deposit'),
    path('login/', cashier_login, name='cashier_login'),
    path('register/', cashier_register, name='cashier_register'),
    path('calculate-interest/', calculate_interest, name='calculate_interest'),
    path('usereg/', user_login, name='user_login'),
    path('userd/', user_reg, name='user_reg'),
    path('success/',success,name='success'),
    path('x/',user_success,name='user_success'),
    path('user/',userp,name="userp"),
    path('user_dashboard/',user_dashboard,name="user_dashboard"),
    path('search-accounts/', search_accounts, name='search_accounts'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)