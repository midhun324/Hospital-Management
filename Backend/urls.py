from django.urls import path
from Backend import views


urlpatterns=[


    path('doctor/',views.doctor,name="doctor"),
    path('index/',views.index,name="index"),
    path('doctor_reg/',views.doctor_reg,name="doctor_reg"),
    path('dotors_record/',views.dotors_record,name="dotors_record"),
    path('edit_doctor/<int:dataid>',views.edit_doctor,name="edit_doctor"),
    path('delete_doc/<int:dataid>',views.delete_doc,name="delete_doc"),
    path('update_doc/<int:dataid>',views.update_doc,name="update_doc"),
    path('view_doctor/', views.view_doctor, name="view_doctor"),
    path('Login_page/', views.Login_page, name="Login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('department/', views.department, name="department"),
    path('save_dept/', views.save_dept, name="save_dept"),
    path('dept_details/', views.dept_details, name="dept_details"),
    path('edit_dept/<int:dept_id>', views.edit_dept, name="edit_dept"),
    path('update_dept/<int:dept_id>', views.update_dept, name="update_dept"),
    path('delete_dept/<int:dept_id>', views.delete_dept, name="delete_dept"),
    path('appointment_details/', views.appointment_details, name="appointment_details"),
    path('delete_ap/<int:ap_id>', views.delete_ap, name="delete_ap"),

]