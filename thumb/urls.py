from django.urls import path,include
from . import views
# from rest_framework import routers


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


# urlpatterns = [
#     path('answer/', AnswerViewSet.list(),name='answer'),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# router = routers.DefaultRouter()


urlpatterns = [
    # path('', include(router.urls)),
    path('question/',views.Question_output,name = 'question'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]