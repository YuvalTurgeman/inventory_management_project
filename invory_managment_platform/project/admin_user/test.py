from django.test import TestCase, RequestFactory
from .models import User
from django.urls import reverse
from .views import register, signin, index, user_login
from django.http import HttpResponse, HttpRequest

class Test_register(TestCase):
    def test_register_create_user(self):
        self.user = User(full_name='shay lavi', id_number='319067613', role='student', email='ahkcht98@gmail.com',
                         password='s5d66342')
        self.user.save()

    def test_register_page_open(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all/signup.html')

    def test_register_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('all/signup')
        response = register(request)
        self.assertEqual(response.status_code, 200)


class Test_login(TestCase):

    def test_login_create_user(self):
        self.user = User(full_name='shay lavi', id_number='319067613', role='student', email='ahkcht98@gmail.com',
                         password='s5d66342')
        self.user.save()

    def test_login_page_open(self):
        url = reverse('signin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all/signin.html')

    def test_login_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('all/signin')
        response = signin(request)
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        request = RequestFactory().get('all/signin.html')
        request.content_params = {'email' : 'ahkcht98@gmail.com','password': 's5d66342'}
        request.method = 'POST'
        response = user_login(request)
        self.assertEqual(response.status_code, 200)


class Test_index(TestCase):
    def test_login_page_open(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/index.html')

    def test_login_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('all/index')
        response = index(request)
        self.assertEqual(response.status_code, 200)
