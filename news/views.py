from rest_framework import generics
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import fetch_news, summarize_text
from .models import SavedArticle
from .serializers import SavedArticleSerializer
from django.contrib.auth.models import User

class LatestNewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = fetch_news("top-headlines?country=in")
        summarized = []
        for article in articles[:5]:
            summary = summarize_text(article.get("content") or article.get("description", ""))
            summarized.append({
                "title": article["title"],
                "url": article["url"],
                "summary": summary
            })
        return Response(summarized)

class SearchNewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '')
        articles = fetch_news(f"everything?q={query}")
        summarized = []
        for article in articles[:5]:
            summary = summarize_text(article.get("content") or article.get("description", ""))
            summarized.append({
                "title": article["title"],
                "url": article["url"],
                "summary": summary
            })
        return Response(summarized)

class SaveArticleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SavedArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class SavedArticlesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = SavedArticle.objects.filter(user=request.user)
        serializer = SavedArticleSerializer(articles, many=True)
        return Response(serializer.data)
