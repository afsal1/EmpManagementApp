from django.db import DatabaseError
from rest_framework.views import APIView
from utilities.mixins import HttpResponseMixin
from utilities.jwt_handler import get_tokens_for_user
from .serializers import RegistrationSerializer, UserLoginSerializer, \
    ViewEmployeesSerializer
from .models import CustomUser
from django.http.response import JsonResponse







class UserRegistrationView(APIView, HttpResponseMixin):
    """
    Class Name: UserRegistrationView
    description: Manage user registration
    """

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        """
        Function Name: post
        description: User registration
        Params: email, password, first name, 
                last name, user_role, emp_code
        Return: access_token,refresh token, user details
        """
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                count = CustomUser.objects.all().count() + 1
                user = serializer.save()
                user.emp_code = f"L{user.first_name[:2]}{count}"
                user.save()
                tokens = get_tokens_for_user(user)
                data = {
                    "access_token": tokens.get("access_token"),
                    "refresh_token": tokens.get("refresh_token"),
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "user_role":user.user_role,
                    "emp_code":user.emp_code
                }

                return self.success_response(
                    data=data,
                    code="HTTP_201_CREATED",
                    message="User registered successfully",
                )
            else:
                return self.success_response(
                    code="HTTP_400_BAD_REQUEST", message=serializer.errors
                )
        except: 
            return JsonResponse('Something went wrong',
                                 safe=False)


class UserLoginView(APIView, HttpResponseMixin):

    """
    Class Name: UserLoginView
    description: Manage user login
    """

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        """
        Function Name: post
        description: User login activity
        Params: email, password
        Return: access_token, refresh token, user details
        """
        try:
            serializer = UserLoginSerializer(data=request.data)
            if serializer.is_valid():
                return JsonResponse(serializer.validated_data, safe=False)

            return self.success_response(
                code="HTTP_400_BAD_REQUEST",
                message=serializer.errors,
            )
        except Exception as e:
            return self.error_response(
                code="HTTP_400_BAD_REQUEST",
                message=f"Something went wrong, Exact Probrlem: {e}",
            )


class UserHomePageView(APIView, HttpResponseMixin):

    """
    Class Name: UserHomePageView
    description: user home page view
    """

    def get(self, request):
        """
        Function Name: get
        description: User home page
        Params: no
        Return: welcome message for user
        """
        try:
            user = request.user
            username = f"{user.first_name} {user.last_name}"
            return self.success_response(
                    data=username,
                    code="HTTP_200_OK",
                    message="Username fetched successfully",
                )
        except Exception as e: 
            return self.error_response(
                code="HTTP_400_BAD_REQUEST",
                message=f"Something went wrong, Exact Probrlem: {e}",
            )


class AdminEmployeesView(APIView, HttpResponseMixin):
    """
    Class Name: AdminEmployeesView
    description: admin can view all employees
    """

    def get(self, request):
        """
        Function Name: get
        description: view all employees
        Params: no
        Return: all employee list
        """
        try:
            employees = CustomUser.objects.filter(user_role="User")
            serializer = ViewEmployeesSerializer(employees, many=True)
            
            return JsonResponse(serializer.data, safe=False)
        except Exception as e: 
            return self.error_response(
                code="HTTP_400_BAD_REQUEST",
                message=f"Something went wrong, Exact Probrlem: {e}",
            )


class AdminViewSingleEmployee(APIView, HttpResponseMixin):
    """
    Class Name: AdminViewSingleEmployee
    description: admin can view a employee details
    """
    def get(self, request, *args, **kwargs):
        """
        Function Name: get
        description: view a employee details
        Params: emp_id
        Return: employee details
        """
        try:
            employee = CustomUser.objects.get(id=kwargs.get("emp_id"))
            serializer = ViewEmployeesSerializer(employee)
            return self.success_response(
                    data=serializer.data,
                    code="HTTP_200_OK",
                    message="employee details fetched successfully",
                )
        except Exception as e: 
            return self.error_response(
                code="HTTP_400_BAD_REQUEST",
                message=f"Something went wrong, Exact Probrlem: {e}",
            )


class AdminEmployeeUpdateDeleteView(APIView, HttpResponseMixin):
    """
    Class Name: AdminEmployeeUpdateDeleteView
    description: admin can update employee details
    """
    permission_classes = ()
    authentication_classes = ()
    def patch(self, request, *args, **kwargs):
        """
        Function Name: patch
        description: update employee details
        Params: emp_id
        Return: success response
        """
        try:
            employee = CustomUser.objects.get(id=kwargs.get("emp_id"))
            data = request.data
            employee.first_name = (
                data["first_name"] if data.get("first_name", None) else employee.first_name
            )
            employee.last_name = (
                data["last_name"] if data.get("last_name", None) else employee.last_name
            )
            employee.user_role = (
                data["user_role"] if data.get("user_role", None) else employee.user_role
            )
            employee.save()
            return self.success_response(
                    code="HTTP_200_OK",
                    message="employee details updated successfully",
                )
        except Exception as e: 
            return self.error_response(
                code="HTTP_400_BAD_REQUEST",
                message=f"Something went wrong, Exact Probrlem: {e}",
            )


    def delete(self, request, *args, **kwargs):
        """
        Function Name: delete
        description: delete employee
        Params: emp_id
        Return: success response
        """
        try:
            CustomUser.objects.get(id=kwargs.get("emp_id")).delete()
            return self.success_response(
                    code="HTTP_200_OK",
                    message="employee deleted successfully",
                )
        except Exception as e: 
            return self.error_response(
                code="HTTP_400_BAD_REQUEST",
                message=f"Something went wrong, Exact Probrlem: {e}",
            )