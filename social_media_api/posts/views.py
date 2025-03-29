from rest_framework import viewsets, generics, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
         following_users = self.request.user.following.all()
         return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk, *args, **kwargs):
         post = generics.get_object_or_404(Post, pk=pk)
         like, created = Like.objects.get_or_create(user=request.user, post=post)
         if not created:
             return Response({'detail': 'Already liked.'}, status=status.HTTP_400_BAD_REQUEST)
         if post.author != request.user:
             Notification.objects.create(recipient=post.author, actor=request.user, verb='liked', target=post)
         return Response({'detail': 'Post liked.'}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk, *args, **kwargs):
         post = generics.get_object_or_404(Post, pk=pk)
         like = Like.objects.filter(user=request.user, post=post).first()
         if not like:
             return Response({'detail': 'Not liked yet.'}, status=status.HTTP_400_BAD_REQUEST)
         like.delete()
         return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
