from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Count, Prefetch, OuterRef, Subquery
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.db.models.functions import Random

class PostPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = Post.objects.annotate(
            comment_count=Count('comments')
        ).prefetch_related(
            Prefetch(
                'comments',
                queryset=Comment.objects.select_related('user').order_by('-timestamp'),
                to_attr='latest_comments'
            )
        ).select_related('user').order_by('-timestamp')
        
        return queryset

    def get_comments(self, obj):
        return CommentSerializer(obj.latest_comments[:3], many=True).data