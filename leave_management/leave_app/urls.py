from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    #student
    path('studentsignup/',views.student_signup,name="studentsignup"),
    path('studentlogin/', views.student_login, name='student_login'),
    path('studentlog', views.student_log, name='student_log'),
    path('stdpage/', views.std_page, name='std_page'),
    path('stddetails/', views.std_details, name='std_details'),
    path('update/<str:pk>', views.update, name="update"),
    path('addleave/', views.add_leave, name='add_leave'),
    path('stdviewstatus/', views.stdview_status, name='stdview_status'),
    path('student_logout/', views.student_logout, name='student_logout'),

    #teacher
    path('teacherreg/', views.teacher_reg, name='teacher_reg'),
    path('teacherlogin/', views.teacher_login, name='teacher_login'),
    path('teacherlog', views.teacher_log, name='teacher_log'),
    path('teacherpage/', views.teacher_page, name='teacher_page'),
    path('viewstd/', views.view_std, name='view_std'),
    path('viewreq/', views.view_req, name='view_req'),
    path('approveleave/<str:username>/', views.approve_leave, name='approve_leave'),
    path('teacher_logout/', views.teacher_logout, name='teacher_logout'),
]