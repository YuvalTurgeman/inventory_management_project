from django.test import TestCase, RequestFactory
from .models import User, Product,Transfers, Expense
from django.urls import reverse
from . import views
from django.utils import timezone
from django.http import HttpResponse, HttpRequest


class Test_register(TestCase):
    def test_register_create_user(self):
        self.user = User(full_name='shay lavi', id_number='319067613', role='student', email='ahkcht98@gmail.com',
                         password='s5d66342')
        self.user.save()

    def test_register_page_open(self):
        url = reverse(views.register)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all/signup.html')

    def test_register_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('all/signup')
        response = views.register(request)
        self.assertEqual(response.status_code, 200)


class Test_login(TestCase):

    def test_login_create_user(self):
        self.user = User(full_name='shay lavi', id_number='319067613', role='student', email='ahkcht98@gmail.com',
                         password='s5d66342')
        self.user.save()

    def test_login_page_open(self):
        url = reverse(views.signin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all/signin.html')

    def test_login_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('all/signin')
        response = views.signin(request)
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        request = RequestFactory().get('all/signin.html')
        request.content_params = {'email': 'ahkcht98@gmail.com', 'password': 's5d66342'}
        request.method = 'POST'
        response = views.user_login(request)
        self.assertEqual(response.status_code, 200)


# ------------------- ADMIN TEST --------------------------
class Test_index_admin(TestCase):
    def test_index_page_open(self):
        url = reverse(views.index)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/index.html')

    def test_index_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/index')
        response = views.index(request)
        self.assertEqual(response.status_code, 200)

class test_productlist_admin(TestCase):
    def test_productlist_page_open(self):
        url = reverse(views.productlist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/productlist.html')

    def test_productlist_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/productlist')
        response = views.index(request)
        self.assertEqual(response.status_code, 200)

class test_addproduct_admin(TestCase):

    def test_addproduct_page_open(self):
        url = reverse(views.addproduct)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/addproduct.html')

    def test_addproduct_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/addproduct')
        response = views.addproduct(request)
        self.assertEqual(response.status_code, 200)

class test_userlist_admin(TestCase):

    def test_userlist_page_open(self):
        url = reverse(views.userlist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/userlist.html')

    def test_userlist_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/userlist')
        response = views.userlist(request)
        self.assertEqual(response.status_code, 200)

class test_adduser_admin(TestCase):

    def test_adduser_page_open(self):
        url = reverse(views.adduser)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/adduser.html')

    def test_adduser_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/adduser')
        response = views.adduser(request)
        self.assertEqual(response.status_code, 200)


# +++++++++++++++++++++ pk testim +++++++++++++++++++++++ #
 
class test_editTransfer_admin(TestCase):
    def setUp(self):
        CHOICES = [('Returned', 'Returned'), ('Loaned', 'Loaned')]
        self.user = Transfers(product_name='shay', category='meow', brand='bobol', to='moiishe',
                    status= 'big', start_of_loan = timezone.now(), end_of_loan  = timezone.now(),
                    qyt = "choke")
        self.user.save()
    def test_editTransfer_page_open(self):
        p = self.user.pk
        url = reverse('editTransfer', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/edittransfer.html')
    def test_editTransfer_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('admin_u/editTransfer')
        response = views.editTransfer(request,p)
        self.assertEqual(response.status_code, 200)


"""
class test_editsupplier_admin(TestCase):
"""
class test_editexpense_admin(TestCase):
    def setUp(self):
        self.user = Expense(description='text text', reference='blabla', date=timezone.now(), price='69')
        self.user.save()
    def test_editexpense_page_open(self):
        p = self.user.pk
        url = reverse(views.editexpense, args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/editexpense.html')
    def test_editexpense_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('admin_u/editexpense')
        response = views.editexpense(request,p)
        self.assertEqual(response.status_code, 200)
"""
class test_editproduct_admin(TestCase):
    def setUp(self):
        self.user = Product(product_name='shay', category='meow', brand='bobol', price='1997',
                              unit='big', qty= ' 159', created_by= ' jon', adding_date = timezone.now())
        self.user.save()

    def test_editproduct_page_open(self):
        p = self.user.pk
        url = reverse(views.edit, args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/editproduct.html')

    def test_editproduct_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('admin_u/editItem')
        response = views.editItem(request, p)
        self.assertEqual(response.status_code, 200)
"""
'''
class test_edituser_admin(TestCase):
    def setUp(self):
        self.user = User(full_name='joni c', id_number='852369741', role='student', email='jonjon@yahoo.com',
                            password='158357852')
        self.user.save()

    def test_edituser_page_open(self):
        p = self.user.pk
        url = reverse(views.edit, args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/editproduct.html')

    def test_edituser_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('admin_u/editItem')
        response = views.editItem(request, p)
        self.assertEqual(response.status_code, 200)
    
'''

class test_saleslist_admin(TestCase):
    def test_saleslist_page_open(self):
        url = reverse(views.saleslist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/saleslist.html')
    def test_saleslist_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/saleslist')
        response = views.saleslist(request)
        self.assertEqual(response.status_code, 200)


class test_addpurchase_admin(TestCase):
    def test_addpurchase_page_open(self):
        url = reverse(views.addpurchase)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/addpurchase.html')

    def test_addpurchase_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/addproduct')
        response = views.addpurchase(request)
        self.assertEqual(response.status_code, 200)

"""
class test_addsupplier_admin(TestCase):
    def test_addsupplier_page_open(self):
        url = reverse(views.addsupplier)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/addsupplier.html')

    def test_addsupplier_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/addsupplier')
        response = views.addsupplier(request)
        self.assertEqual(response.status_code, 200)
"""
class test_chart_apex_admin(TestCase):
    def test_chart_apex_page_open(self):
        url = reverse(views.chart_apex)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/chart-apex.html')

    def test_chart_apex_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/chart_apex')
        response = views.chart_apex(request)
        self.assertEqual(response.status_code, 200)

class test_createexpense_admin(TestCase):
    def test_createexpense_page_open(self):
        url = reverse(views.createexpense)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/createexpense.html')

    def test_createexpense_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/createexpense')
        response = views.createexpense(request)
        self.assertEqual(response.status_code, 200)

class test_expenselist_admin(TestCase):
    def test_expenselist_page_open(self):
        url = reverse(views.expenselist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/expenselist.html')

    def test_expenselist_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/expenselist')
        response = views.expenselist(request)
        self.assertEqual(response.status_code, 200)

class test_inventoryreport_admin(TestCase):
    def test_inventoryreport_page_open(self):
        url = reverse(views.inventoryreport)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/inventoryreport.html')

    def test_inventoryreport_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/inventoryreport')
        response = views.inventoryreport(request)
        self.assertEqual(response.status_code, 200)

class test_purchaselist_admin(TestCase):
    def test_purchaselist_page_open(self):
        url = reverse(views.purchaselist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/purchaselist.html')

    def test_purchaselist_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/purchaselist')
        response = views.purchaselist(request)
        self.assertEqual(response.status_code, 200)

class test_purchaseorderreport_admin(TestCase):
    def test_purchaseorderreport_page_open(self):
        url = reverse(views.purchaseorderreport)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/purchaseorderreport.html')

    def test_purchaseorderreport_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/purchaseorderreport')
        response = views.purchaseorderreport(request)
        self.assertEqual(response.status_code, 200)

class test_purchasereport_admin(TestCase):
    def test_purchasereport_page_open(self):
        url = reverse(views.purchasereport)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/purchasereport.html')

    def test_purchasereport_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/purchasereport')
        response = views.purchasereport(request)
        self.assertEqual(response.status_code, 200)

class test_salesreport_admin(TestCase):
    def test_salesreport_page_open(self):
        url = reverse(views.salesreport)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/salesreport.html')

    def test_salesreport_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/salesreport')
        response = views.salesreport(request)
        self.assertEqual(response.status_code, 200)

class test_supplierlist_admin(TestCase):
    def test_supplierlist_page_open(self):
        url = reverse(views.supplierlist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/supplierlist.html')

    def test_supplierlist_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('admin_u/supplierlist')
        response = views.supplierlist(request)
        self.assertEqual(response.status_code, 200)

# edit

# ------------------- STUDENT TEST --------------------------
class Test_index_student(TestCase):

    def test_indexs_page_open(self):
        url = reverse(views.indexs)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/index.html')

    def test_indexs_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/index')
        response = views.indexs(request)
        self.assertEqual(response.status_code, 200)

class Test_chart_apexs_student(TestCase):
    def test_chart_apexs_page_open(self):
        url = reverse(views.chart_apexs)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/chart-apex.html')

    def test_chart_apexs_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/chart-apexs')
        response = views.chart_apexs(request)
        self.assertEqual(response.status_code, 200)

# ------------------- TEACHER TEST --------------------------
