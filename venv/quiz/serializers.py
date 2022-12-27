from rest_framework import serializers
from .models import Quiz

# serializer는 장고 모델 데이터를 JSON 타입으로 바꿔주는(직렬화) 코드

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')