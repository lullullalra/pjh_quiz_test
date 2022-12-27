from django.urls import path, include
from .views import helloAPI, randomQuiz

# quiz app에 대한 url 관리
# myapi/urls.py는 전체 프로젝트 url 관리
# quiz/urls.py 먼저 설정 후 myapi/urls.py 설정

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]

