from rest_framework import serializers
from quiz.models import Quiz,Category,Option, OptionList

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = 'id name description'.split()

class CategorySerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = Category
        fields = 'id name options '.split()

class QuizSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = Quiz
        fields = 'id name categories'.split()

    def get_options(self,obj):
        options = Quiz.objects.filter(quiz=obj)
        return OptionSerializer(options,many=True).data

class QuestionListSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Option
        fields = ['id', 'name', 'description','category']



class OptionMTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionList
        fields = ['id','options_post_answers']


