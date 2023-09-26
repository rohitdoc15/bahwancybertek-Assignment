from django.contrib.auth.models import User
from .models import Post
from .serializers import UserRegistrationSerializer, PostSerializer
from rest_framework import generics, permissions

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from django.shortcuts import render
from .models import Post, Profile

from django.http import JsonResponse

from django.http import JsonResponse
from django.contrib.auth.models import User

from django.shortcuts import render
from django.contrib.auth.models import User

def homepage(request):
    users_data = [
        {
            "username": user.username,
            "post_count": Post.objects.filter(author=user).count(),
            "followers_count": user.profile.followers.count() if hasattr(user, 'profile') else 0,
            "following_count": user.profile.following.count() if hasattr(user, 'profile') else 0
        }
        for user in User.objects.all()
    ]

    context = {"users_data": users_data}
    return render(request, "homepage.html", context)
