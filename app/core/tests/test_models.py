from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """Custom user model that suppors using email instead of username"""

        email = "test@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Custom user model that suppors using a normalized email"""

        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "testpass123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Custom user model with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "testpass123")

    def test_create_new_super_user(self):
        """Creates and saves a new super user"""

        user = get_user_model().objects.create_superuser(
            "test@gmail.com", "testpass123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
