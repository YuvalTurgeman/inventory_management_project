"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from admin_user import views
#aaaaaa
urlpatterns = [
    path('admin/', admin.site.urls, name=admin),
    path('', views.signin, name='signin'),
    path("register/", views.register, name="register"),
    path("admin_user/", include("admin_user.urls")),
    path("index/", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("productlist/", views.productlist, name="productlist"),
    path("deleteItem/(?P<pk>\d+)/", views.deleteItem, name="deleteItem"),
    path("editItem/(?P<pk>\d+)/", views.editItem, name="editItem"),
    path("addproduct/", views.addproduct, name="addproduct"),
    path("saleslist/", views.saleslist, name="saleslist"),
    path("deleteTransfer/(?P<pk>\d+)/", views.deleteTransfer, name="deleteTransfer"),
    path("editTransfer/(?P<pk>\d+)/", views.editTransfer, name="editTransfer"),
    path("purchaselist/", views.purchaselist, name="purchaselist"),
    path("deletePurchase/(?P<pk>\d+)/", views.deletePurchase, name="deletePurchase"),
    path("addpurchase/", views.addpurchase, name="addpurchase"),
    path("expenselist/", views.expenselist, name="expenselist"),
    path("editexpense/(?P<pk>\d+)/", views.editexpense, name="editexpense"),
    path("createexpense/", views.createexpense, name="createexpense"),
    path("deleteExpense/(?P<pk>\d+)/", views.deleteExpense, name="deleteExpense"),
    path("supplierlist/", views.supplierlist, name="supplierlist"),
    path("addsupplier/", views.addsupplier, name="addsupplier"),
    path("deleteSupplier/(?P<pk>\d+)/", views.deleteSupplier, name="deleteSupplier"),
    path("editSupplier/(?P<pk>\d+)/", views.editSupplier, name="editSupplier"),
    path("userlist/", views.userlist, name="userlist"),
    path("adduser/", views.adduser, name="adduser"),
    path("deleteUser/(?P<pk>\d+)/", views.deleteUser, name="deleteUser"),
    path("editUser/(?P<pk>\d+)/", views.editUser, name="editUser"),
    path("inventoryreport/", views.inventoryreport, name="inventoryreport"),
    path("salesreport/", views.salesreport, name="salesreport"),
    path("purchasereport/", views.purchasereport, name="purchasereport"),
    path("chart-apex/", views.chart_apex, name="chart-apex"),
    path("purchaseorderreport/", views.purchaseorderreport, name="purchaseorderreport"),

    path("indexs/", views.indexs, name="indexs"),
    path("productlists/", views.productlists, name="productlists"),
    path("addproducts/", views.addproducts, name="addproducts"),
    path("saleslists/", views.saleslists, name="saleslists"),
    path("purchaselists/", views.purchaselists, name="purchaselists"),
    path("quotationlists/", views.quotationlists, name="quotationlists"),
    path("addquotations/", views.addquotations, name="addquotations"),
    path("supplierlists/", views.supplierlists, name="supplierlists"),
    path("userlists/", views.userlists, name="userlists"),
    path("inventoryreports/", views.inventoryreports, name="inventoryreports"),
    path("salesreports/", views.salesreports, name="salesreports"),
    path("purchasereports/", views.purchasereports, name="purchasereports"),
    path("chart-apexs/", views.chart_apexs, name="chart-apexs"),
    path("purchaseorderreports/", views.purchaseorderreports, name="purchaseorderreports"),

    path("productlistt/", views.productlistt, name="productlistt"),
    path("saleslistt/", views.saleslistt, name="saleslistt"),
    path("purchaselistt/", views.purchaselistt, name="purchaselistt"),
    path("expenselistt/", views.expenselistt, name="expenselistt"),
    path("quotationlistt/", views.quotationlistt, name="quotationlistt"),
    path("addquotationt/", views.addquotationt, name="addquotationt"),
    path("supplierlistt/", views.supplierlistt, name="supplierlistt"),
    path("userlistt/", views.userlistt, name="userlistt"),
    path("inventoryreportt/", views.inventoryreportt, name="inventoryreportt"),
    path("salesreportt/", views.salesreport, name="salesreportt"),
    path("purchasereportt/", views.purchasereport, name="purchasereportt"),
    path("chart-apext/", views.chart_apext, name="chart-apext"),
    path("purchaseorderreport/", views.purchaseorderreportt, name="purchaseorderreportt"),
    path("addusert/", views.addusert, name="addusert"),

]
