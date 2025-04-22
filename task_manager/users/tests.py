from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserTest(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.client.force_login(self.user)

    def test_create_user(self):
        response = self.client.post(reverse('user_create'), {
            'first_name': 'Ivan',
            'last_name': 'Petrov',
            'username': 'ivanpetrov',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='ivanpetrov').exists())

    def test_update_user(self):
        user = User.objects.get(pk=2)
        response = self.client.post(reverse('user_update', 
                                            kwargs={'pk': self.user.pk}),
                                            {'first_name': 'TestName',
                                             'last_name': user.last_name,
                                             'username': user.username,
                                            })
        user.refresh_from_db()
        self.assertEqual(user.first_name, "TestName")
        self.assertEqual(response.status_code, 302)

    def test_delete_user(self):
        user = User.objects.get(pk=2)
        response = self.client.post(reverse("user_delete", 
                                            kwargs={'pk': user.pk,
                                                    }))
        self.assertFalse(User.objects.filter(pk=2).exists())
        self.assertEqual(response.status_code, 302)
