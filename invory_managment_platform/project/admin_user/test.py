from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import register, signin, index, user_login, indexs, indext


class Test_register(TestCase):

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

    def test_register_empty_person(self):
        data = {}
        request = RequestFactory().post('all/signup.html', data)
        request.method = 'POST'
        response = register(request)
        self.assertEqual(response.status_code, 200)

    def test_register_not_valid_person(self):
        data = {'email': 'admin2345@gmail.com', 'password': 's5d66342', 'role': 'admin'}
        request = RequestFactory().post('all/signup.html', data)
        request.method = 'POST'
        response = register(request)
        self.assertEqual(response.status_code, 200)


class Test_login(TestCase):

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

    def test_login_not_empty_user(self):
        request = RequestFactory().get('all/signin.html')
        request.method = 'POST'
        response = user_login(request)
        self.assertEqual(response.status_code, 200)

    def test_login_not_valid_user(self):
        data = {'email': 'admin2345@gmail.com', 'password': 's5d66342'}
        request = RequestFactory().post('all/signin.html', data)
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
        request = factory.get('admin_u/index')
        response = index(request)
        self.assertEqual(response.status_code, 200)


class Test_index_teacher(TestCase):
    def test_login_page_open(self):
        url = reverse('indext')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/index.html')

    def test_login_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/index')
        response = indext(request)
        self.assertEqual(response.status_code, 200)

