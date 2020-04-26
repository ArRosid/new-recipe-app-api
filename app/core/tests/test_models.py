from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@gmail.com"
        password = "TestPassword@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # default nya create user akan minta argumen username,
        # tapi nanti kita akan override fungsi create_user

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "TestPassword@123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'testsuperuser@gmail.com',
            'test1234'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        # is super user itu tidak ada di model user,
        # tapi ada di permission mixins
