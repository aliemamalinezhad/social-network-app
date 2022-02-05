from django.test import TestCase
from posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class TestModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@gmail.com', username='test_user',
            first_name='jack', last_name='jackson',
            phone='09100000000', password='ali123456',
        )
        self.post = Post.objects.create(
            author=self.user, title="test title",
            text="test text", slug="test-title",
        )

    def test_post_create(self):
        self.assertEqual(self.post.title, "test title")
