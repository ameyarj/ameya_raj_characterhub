from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'timestamp', 'author_username']

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='user.username')
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'author_username', 'comments', 'comment_count']

    def get_comments(self, obj):
        return CommentSerializer(obj.latest_comments[:3], many=True).data

    def get_comment_count(self, obj):
        return obj.comment_count
