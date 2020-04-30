from django.shortcuts import render


from api.models import Category, Article
from api.serializers import CategorySerializer, ArticleSerialize
from rest_framework.views import APIView, status
from rest_framework.response import Response

class CategoryListView(APIView):
    def get(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        Category.objects.create(
            name = request.data['name']
        )
        return Response({"":"successs"}, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view
@api_view(['GET'])
def articles(request):
    articles = Article.objects.all()
    serializer = 





