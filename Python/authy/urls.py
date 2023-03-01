from django.urls import path
from . import views


urlpatterns = [
    path(
        "user_register_view/",
        views.UserRegistrationView.as_view(),
        name="user_register_view",
    ),
    path(
        "user_login_view/",
        views.UserLoginView.as_view(),
        name="user_login_view",
    ),
    path(
        "user_home_view/",
        views.UserHomePageView.as_view(),
        name="user_home_view",
    ),
    path(
        "employee/",
        views.AdminEmployeesView.as_view(),
        name="employee",
    ),
    path(
        "single_employee/<slug:emp_id>/",
        views.AdminViewSingleEmployee.as_view(),
        name="single_employee",
    ),
    path(
        "update_delete_employee/<slug:emp_id>/",
        views.AdminEmployeeUpdateDeleteView.as_view(),
        name="update_delete_employee",
    ),
]