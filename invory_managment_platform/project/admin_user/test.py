from django.test import TestCase, RequestFactory
from .models import User_Data, Product,Transfers, Expense, Supplier
from django.urls import reverse
from . import views
from django.utils import timezone
from django.http import HttpResponse, HttpRequest


class Test_register(TestCase):
    def test_register_create_user(self):
        self.user = User_Data(full_name='shay lavi', id_number='319067613', role='student', email='ahkcht98@gmail.com',
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
        self.user = User_Data(full_name='shay lavi', id_number='319067613', role='student', email='ahkcht98@gmail.com',
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


# ------------------- ADMIN TESTS --------------------------
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
        response = views.productlist(request)
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


# +++++++++++++++++++++ PK TESTS +++++++++++++++++++++++ #
 
class test_editTransfer_admin(TestCase):
    def setUp(self):
        self.user = Transfers(product_name='prod_name', category='category', brand='brand', to='to',
                    status= 'status', start_of_loan = timezone.now(), end_of_loan  = timezone.now(),
                    qyt = "qyt")
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

class test_editsupplier_admin(TestCase):
    def setUp(self):
        self.user = Supplier(supplier_name='pablo escobar', code='15935786', phone="420420420", email='soher@gov.il',
                             country='columbia')
        self.user.save()
    def test_editsupplier_page_open(self):
        p = self.user.pk
        url = reverse(views.editSupplier, args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/editsupplier.html')
    def test_editsupplier_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('admin_u/editSupplier')
        response = views.editSupplier(request, p)
        self.assertEqual(response.status_code, 200)

class test_editexpense_admin(TestCase):
    def setUp(self):
        self.user = Expense(description='TEXTTXET', reference='recipe', date=timezone.now(), price='20')
        self.user.save()
    def test_editexpense_page_open(self):
        url = reverse(views.editexpense, args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/editexpense.html')
    def test_editexpense_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('admin_u/editexpense')
        response = views.editexpense(request, p)
        self.assertEqual(response.status_code, 200)


class test_editproduct_admin(TestCase):
    def setUp(self):
        self.user = Product(product_name='pen', category='ball', brand='c4', price='10',
                              unit='small', qty= ' 1', created_by= ' jon', adding_date = timezone.now())
        self.user.save()

    def test_editproduct_page_open(self):
        p = self.user.pk
        url = reverse(views.editItem, args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/editproduct.html')

    def test_editproduct_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('admin_u/editItem')
        response = views.editItem(request, p)
        self.assertEqual(response.status_code, 200)

class test_edituser_admin(TestCase):
    def setUp(self):
        self.user = User_Data(full_name='joni c', id_number='852369741', role='student', email='jonjon@yahoo.com',
                            password='158357852')
        self.user.save()

    def test_edituser_page_open(self):
        p = self.user.pk
        url = reverse(views.editUser, args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/edituser.html')

    def test_edituser_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('admin_u/editUser')
        response = views.editUser(request, p)
        self.assertEqual(response.status_code, 200)

# -------------END PK TESTS ADMIN-----------------

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
        request = factory.get('admin_u/addpurchase')
        response = views.addpurchase(request)
        self.assertEqual(response.status_code, 200)

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

# ------------------- TEACHER TESTS --------------------------

class Test_indext_teacher(TestCase):
    def test_indext_page_open(self):
        url = reverse(views.indext)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/index.html')

    def test_indext_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/index')
        response = views.indext(request)
        self.assertEqual(response.status_code, 200)

class test_expenselistt_teacher(TestCase):

    def test_expenselistt_page_open(self):
        url = reverse(views.expenselistt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/expenselist.html')

    def test_expenselistt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/expenselist')
        response = views.expenselistt(request)
        self.assertEqual(response.status_code, 200)


class test_inventoryreportt_teacher(TestCase):
    def test_inventoryreportt_page_open(self):
        url = reverse(views.inventoryreportt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/inventoryreport.html')

    def test_inventoryreportt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/inventoryreport')
        response = views.inventoryreportt(request)
        self.assertEqual(response.status_code, 200)


class test_productlistt_teacher(TestCase):
    def test_productlistt_page_open(self):
        url = reverse(views.productlistt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/productlist.html')

    def test_productlistt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/productlist')
        response = views.productlistt(request)
        self.assertEqual(response.status_code, 200)


class test_purchaselistt_teacher(TestCase):
    def test_purchaselistt_page_open(self):
        url = reverse(views.purchaselistt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/purchaselist.html')

    def test_purchaselistt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/purchaselist')
        response = views.purchaselistt(request)
        self.assertEqual(response.status_code, 200)


class test_purchaseorderreportt_teacher(TestCase):

    def test_purchaseorderreportt_page_open(self):
        url = reverse(views.purchaseorderreportt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/purchaseorderreport.html')

    def test_purchaseorderreportt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/purchaseorderreport')
        response = views.purchaseorderreportt(request)
        self.assertEqual(response.status_code, 200)


class test_purchasereportt_teacher(TestCase):

    def test_purchasereportt_page_open(self):
        url = reverse(views.purchasereportt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/purchasereport.html')

    def test_purchasereportt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/purchasereport')
        response = views.purchasereportt(request)
        self.assertEqual(response.status_code, 200)


class test_saleslistt_teacher(TestCase):

    def test_saleslistt_page_open(self):
        url = reverse(views.saleslistt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/saleslist.html')

    def test_saleslistt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/saleslist')
        response = views.saleslistt(request)
        self.assertEqual(response.status_code, 200)


class test_salesreportt_teacher(TestCase):

    def test_salesreportt_page_open(self):
        url = reverse(views.salesreportt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/salesreport.html')


    def test_salesreportt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/salesreport')
        response = views.salesreportt(request)
        self.assertEqual(response.status_code, 200)


class test_supplierlistt_teacher(TestCase):
    def test_supplierlistt_page_open(self):
        url = reverse(views.supplierlistt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/supplierlist.html')

    def test_supplierlist_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/supplierlist')
        response = views.supplierlistt(request)
        self.assertEqual(response.status_code, 200)


class test_userlistt_teacher(TestCase):

    def test_userlistt_page_open(self):
        url = reverse(views.userlistt)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/userlist.html')

    def test_userlistt_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('teacher/userlist')
        response = views.userlistt(request)
        self.assertEqual(response.status_code, 200)

# +++++++++++++++++++++ PK TESTS +++++++++++++++++++++++ #

class test_editTransfers_student(TestCase):
    def setUp(self):
        self.user = Transfers(product_name='product', category='category', brand='brand', to='to',
                              status='status', start_of_loan=timezone.now(), end_of_loan=timezone.now(),
                              qyt="1")#maybe change to qty, check on thursday if it matters when tunning this test or not
        self.user.save()

    def test_editTransfers_page_open(self):
        p = self.user.pk
        url = reverse('editTransfert', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher/edittransfer.html')

    def test_editTransfers_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('teacher/editTransfer')
        response = views.editTransfert(request, p)
        self.assertEqual(response.status_code, 200)

# -------------END PK TESTS TEACHER-----------------



# ------------------- STUDENT TESTS --------------------------
class Test_indexs_student(TestCase):

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

class test_supplierlists_student(TestCase):
    def test_supplierlists_page_open(self):
        url = reverse(views.supplierlists)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/supplierlist.html')

    def test_supplierlists_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/supplierlist')
        response = views.supplierlists(request)
        self.assertEqual(response.status_code, 200)

class test_salesreports_student(TestCase):
    def test_salesreports_page_open(self):
        url = reverse(views.salesreports)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/salesreport.html')

    def test_salesreports_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/salesreport')
        response = views.salesreports(request)
        self.assertEqual(response.status_code, 200)

class test_saleslists_student(TestCase):
    def test_saleslists_page_open(self):
        url = reverse(views.saleslists)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/saleslist.html')
    def test_saleslists_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('studnet/saleslist')
        response = views.saleslists(request)
        self.assertEqual(response.status_code, 200)

class test_purchaselists_teacher(TestCase):
    def test_purchaselists_page_open(self):
        url = reverse(views.purchaselists)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/purchaselist.html')

    def test_purchaselists_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/purchaselist')
        response = views.purchaselists(request)
        self.assertEqual(response.status_code, 200)

class test_purchaseorderreports_student(TestCase):
    def test_purchaseorderreports_page_open(self):
        url = reverse(views.purchaseorderreports)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/purchaseorderreport.html')

    def test_purchaseorderreports_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/purchaseorderreport')
        response = views.purchaseorderreports(request)
        self.assertEqual(response.status_code, 200)

class test_purchasereports_student(TestCase):
    def test_purchasereports_page_open(self):
        url = reverse(views.purchasereports)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/purchasereport.html')

    def test_purchasereports_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/purchasereport')
        response = views.purchasereports(request)
        self.assertEqual(response.status_code, 200)

class test_productlists_studnet(TestCase):
    def test_productlists_page_open(self):
        url = reverse(views.productlists)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/productlist.html')

    def test_productlists_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/productlist')
        response = views.productlists(request)
        self.assertEqual(response.status_code, 200)

class test_inventoryreports_student(TestCase):
    def test_inventoryreports_page_open(self):
        url = reverse(views.inventoryreport)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_u/inventoryreport.html')

    def test_inventoryreports_view_deployed_to_page(self):
        factory = RequestFactory()
        request = factory.get('student/inventoryreports')
        response = views.inventoryreport(request)
        self.assertEqual(response.status_code, 200)


# +++++++++++++++++++++ PK TESTS +++++++++++++++++++++++ #

class test_editTransfers_student(TestCase):
    def setUp(self):
        self.user = Transfers(product_name='product', category='category', brand='brand', to='to',
                              status='status', start_of_loan=timezone.now(), end_of_loan=timezone.now(),
                              qyt="1")#maybe change to qty, check on thursday if it matters when tunning this test or not
        self.user.save()

    def test_editTransfers_page_open(self):
        p = self.user.pk
        url = reverse('editTransfers', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/edittransfer.html')

    def test_editTransfers_view_deployed_to_page(self):
        p = self.user.pk
        factory = RequestFactory()
        request = factory.get('student/editTransfers')
        response = views.editTransfer(request, p)
        self.assertEqual(response.status_code, 200)

# -------------END PK TESTS STUDENT-----------------
