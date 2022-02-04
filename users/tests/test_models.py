import username as username
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class TestModel(TestCase):
    def setUp(self):
        """Test for create a uesr before setting tests on that user"""
        self.user = User.objects.create_user(email='test@gmail.com', username='test_user',
                                             first_name='jack', last_name='jackson',
                                             phone='09100000000', password='ali123456',
                                             )

    def test_user_create(self):
        """Test the user is created with email address"""
        self.assertEqual(self.user.email, 'test@gmail.com')

    def test_new_user_email_normalized(self):
        """Test the email is normalized"""
        email = 'test2@GMAIL.COM'
        user = User.objects.create_user(
            email=email, username='test_user',
            first_name='jack', last_name='jackson',
            phone='09100000000', password='ali123456',
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email=None, username='test_user',
                first_name='jack', last_name='jackson',
                phone='09100000000', password='ali123456',
            )
