import os
import sys

from decouple import config
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse  # Updated to use JsonResponse
from django.shortcuts import redirect, render
from django.urls import include, path
from django.views.decorators.http import require_http_methods

BASE_DIR = os.path.dirname(__file__)

# Environment Variables
DEBUG = config("DEBUG", default=True, cast=bool)
SECRET_KEY = config("SECRET_KEY", default="your_default_secret_key")
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Django Settings
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    STATIC_URL="/static/",
    STATIC_ROOT=os.path.join(BASE_DIR, "staticfiles"),
    # uncomment this after you have created your database in digitalocean
    # DATABASES={
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql",
    #         "NAME": config("DB_NAME", default="your_default_db_name"),
    #         "USER": config("DB_USER", default="your_default_db_user"),
    #         "PASSWORD": config("DB_PASSWORD", default="your_default_db_password"),
    #         "HOST": config("DB_HOST", default="localhost"),
    #         "PORT": config("DB_PORT", default="5432"),
    #     }
    # },
    INSTALLED_APPS=[
        # compulsory
        "django.contrib.auth",  # For user authentication
        "django.contrib.contenttypes",  # For content types used by the authentication system
        "django.contrib.sessions",  # For session management, required if using session-based authentication
        "django.contrib.staticfiles",  # For serving static files
        # END compulsory
        "django.contrib.admin",  # for admin
        "django.contrib.messages",  # for admin
        "rest_framework",
        "oauth2_provider",
        "corsheaders",  # for oauth
    ],
    ROOT_URLCONF=__name__,
    LOGIN_URL="/admin/login/",  # for auth but using admin
    MIDDLEWARE=[
        "corsheaders.middleware.CorsMiddleware",  # for oauth and before any middleware
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",  # Required for admin
        "django.contrib.auth.middleware.AuthenticationMiddleware",  # Required for admin
        "django.contrib.messages.middleware.MessageMiddleware",  # Required for admin
    ],
    # Templates
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,  # Add this line to enable template loading from plugins
            "OPTIONS": {
                "context_processors": [
                    # ... other context processors ...
                    "django.template.context_processors.debug",  # for admin
                    "django.template.context_processors.request",  # for admin
                    "django.contrib.auth.context_processors.auth",  # for admin
                    "django.contrib.messages.context_processors.messages",  # for admin
                ],
            },
        },
    ],
    CORS_ORIGIN_ALLOW_ALL=True,  # for oauth
    OAUTH2_PROVIDER={  # for oauth"
        "PKCE_REQUIRED": False,  # for gpt because they don't support PKCE
    },
    REST_FRAMEWORK={
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
            # ... other authentication classes ...
        ],
        # ... other DRF settings ...
    },
)


# Ensure django fully utilized before models, etc
import django

django.setup()
# End


# Serializers
# ----

from rest_framework import serializers


class MyDataSerializer(serializers.Serializer):
    field1 = serializers.CharField(max_length=100)
    field2 = serializers.IntegerField()


# end of serializers


# Views
def hello_world(request):
    return JsonResponse({"message": "Hello, World!"})  # Updated endpoint function


from marshmallow import Schema, fields
from webargs.djangoparser import use_args


class NameSchema(Schema):
    name = fields.Str(required=True)


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["POST"])
@use_args(NameSchema(), location="json")
def say_my_name(request, request_args):
    name = request_args.get("name")
    return JsonResponse({"message": f"Hello, {name}"})


def privacy(request):
    return render(request, "privacy.html")


# DRF custom schema
# from rest_framework.schemas.openapi import AutoSchema


# class CustomSchema(AutoSchema):
#     def get_components(self, path, method):
#         components = super().get_components(path, method)
#         # Add your custom components here
#         components["MyData"] = {
#             "type": "object",
#             "properties": {"field1": {"type": "string"}, "field2": {"type": "integer"}},
#         }
#         return components


# DRF view

# from rest_framework.response import Response
# from rest_framework.views import APIView


# class MyDataView(APIView):
#     schema = CustomSchema()

#     def get(self, request):
#         """
#         get:
#           summary: Example endpoint returning a data structure
#           description: An endpoint that returns a simple data structure.
#           responses:
#             200:
#               description: A sample data structure
#               content:
#                 application/json:
#                   schema: MyDataSerializer
#         """
#         # Example data
#         data = {"field1": "value1", "field2": 123}
#         return Response(MyDataSerializer(data).data)


from rest_framework.renderers import JSONOpenAPIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view

# Define the schema view
schema_view = get_schema_view(
    title="Your API",
    version="1.0.0",
    description="Your API description",
    renderer_classes=[JSONOpenAPIRenderer, OpenAPIRenderer],
)

# End of DRF

# Django oAuth Toolkit

from oauth2_provider.decorators import protected_resource
from oauth2_provider.views.generic import ProtectedResourceView


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {"message": "Hello, OAuth2! Talking to you from class based ApiEndpoint"}
        )  # Updated endpoint function


@protected_resource()
def api_endpoint(request):
    return JsonResponse(
        {"message": "Hello, OAuth2! Talking to you from function based api_endpoint"}
    )  # Updated endpoint function


# End of Django oAuth Toolkit

# End of Views


# URL Patterns

from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("", lambda request: redirect("/hello/", permanent=True)),
    path("admin/", admin.site.urls),  # for admin
    path("hello/", hello_world),  # Updated path
    path("privacy/", privacy),  # privacy
    path("say-my-name/", say_my_name),  # say-my-name
    # path("api/mydata/", MyDataView.as_view()),  # DRF
    path("openapi/", schema_view, name="openapi-schema"),
    # path("accounts/", include("django.contrib.auth.urls")),  # for auth
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path(
        "api/class_based/hello", ApiEndpoint.as_view()
    ),  # an example resource endpoint using class based
    path(
        "api/function_based/hello", api_endpoint
    ),  # an example resource endpoint using function based
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
