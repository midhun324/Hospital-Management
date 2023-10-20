from django.urls import path
from FrontEnd import views



urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),

    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('service/',views.service,name="service"),
    path('login_signup/',views.login_signup,name="login_signup"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('make_appointment/',views.make_appointment,name="make_appointment"),
    path('department_pg/',views.department_pg,name="department_pg"),
    path('single_dept/<int:dept_id>',views.single_dept,name="single_dept"),
    path('appointment_page/',views.appointment_page,name="appointment_page"),
    path('make_appointment_2/',views.make_appointment_2,name="make_appointment_2"),
    path('confirmation_pg/',views.confirmation_pg,name="confirmation_pg"),
    path('doctor_page/',views.doctor_page,name="doctor_page"),
    path('single_doctor/<int:doc_id>',views.single_doctor,name="single_doctor"),
    path('user_Logout/',views.user_Logout,name="user_Logout"),
    path('blog_page/',views.blog_page,name="blog_page"),
    path('single_blog/',views.single_blog,name="single_blog"),
    path('save_contact/',views.save_contact,name="save_contact"),
]