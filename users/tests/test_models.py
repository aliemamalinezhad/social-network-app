import username as username
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class TestModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@gmail.com', username='test_user',
                                        first_name='jack', last_name='jackson',
                                        phone='09100000000', password='ali123456',
                                        )

    def test_user_create(self):
        self.assertEqual(self.user.email, 'test@gmail.com')
