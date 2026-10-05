from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:id>/edit/",update_experience,name="update_experience",),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path('education/', show_education, name='show_education'),
    path("education/add", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("education/<uuid:id>/edit/",update_education,name="update_education",),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("education/<uuid:education_id>/star/",education_toggle_star,name="education_toggle_star",),
    path("experience/<uuid:experience_id>/star/",experience_toggle_star,name="experience_toggle_star",),
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
]