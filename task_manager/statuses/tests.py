from django.test import TestCase
from .models import Status
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class StatusTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.status = Status.objects.create(name='teststatus')

    def test_create_status(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse('status_create'), {
            'name': 'Working',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='Working').exists())

    def test_update_status(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse('status_update', kwargs={'pk': self.status.pk}),
                                            {'name': 'New Name',
                                            })
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, "New Name")
        self.assertEqual(response.status_code, 302)


    def test_delete_status(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse("status_delete", kwargs={'pk': self.status.pk}))
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
        self.assertEqual(response.status_code, 302)
