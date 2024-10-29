from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('admin_panel/',views.admin_panel,name='admin_panel'),
    path('login_view/',views.login_view,name='login_view'),
    path('add_student/',views.add_student,name='add_student'),
    path('add_course/',views.add_course,name='add_course'),
    path('show_teachers/',views.show_teachers,name='show_teachers'),
    path('show_students/',views.show_students,name='show_students'),
    path('teacher_reg', views.teacher_reg, name='teacher_reg'),   
    path('teach_home',views.teach_home,name='teach_home'),
    path('logout/',views.logout_view,name='logout'),
    path('editstudent/<int:pk>/',views.editstudent,name='editstudent'),
    path('teacher/edit/<int:pk>/',views.edit_teacher,name='edit_teacher'),
    path('delete_student/<int:pk>/',views.delete_student,name='delete_student'),
    path('delete_teacher/<int:teacher_id>/',views.delete_teacher,name='delete_teacher'),
    path('teacher/profile/', views.teacher_profile, name='teacher_profile'),

]
