#import xlwt as xlwt
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .forms import RegisterForm, ProductForm, TransferForm, PurchasesForm, ExpenseForm, SupplierForm
from django.db.models import Q
from .models import User_Data, ValidId, Product, Purchases, Finance, Transfers, Expense, Supplier
from datetime import datetime


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        id = request.POST.get('id_number')
        role = request.POST.get('role')
        form = RegisterForm(request.POST)
        mydata = ValidId.objects.filter(Q(role=role) & Q(id_number=id)).values()
        mydataUnique = User_Data.objects.filter(Q(email=email) | Q(id_number=id)).values()
        if len(mydataUnique) == 0 and mydata:
            if form.is_valid():
                form.save()
                return render(request, 'all/signin.html')
            else:
                print("Invalid login details supplied.")
                return HttpResponse("Invalid login details supplied.")
        else:
            print("Invalid login details supplied.")
            return HttpResponse("Invalid login details supplied.")

    context = {'form': form}
    return render(request, 'all/signup.html', context)


def signin(request):
    return render(request, 'all/signin.html')


def index(request):
    date = datetime.now()
    data = {
        'users_num': len(User_Data.objects.all()),
        'returned_items': len(Transfers.objects.filter(Q(status='Returned')).values()),
        'budget': Finance.objects.all(),
        'total_purchase': Finance.objects.all(),
        'purchase_items': len(Purchases.objects.all()),
        'transfers': len(Transfers.objects.all()),
        "products": Product.objects.filter(Q(adding_date=date)).values(),
        'transfersp': Transfers.objects.filter(Q(start_of_loan=date) | Q(end_of_loan=date)).values(),
    }
    return render(request, 'admin_u/index.html', data)


def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        email = request.POST.get('email')
        password = request.POST.get('password')
        mydata = User_Data.objects.filter(Q(email=email) & Q(password=password)).values()
        if mydata.filter(role='student'):
            return indexs(request)

        if mydata.filter(role='admin'):
            return index(request)

        if mydata.filter(role='teacher'):
            return indext(request)

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details supplied.")


def productlist(request):
    data = {
        "products": Product.objects.all(),
    }
    return render(request, 'admin_u/productlist.html', data)


def editItem(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        data = {
            "products": Product.objects.all(),
        }
        return render(request, 'admin_u/productlist.html', data)
    context = {'form': form, 'product': product}
    return render(request, 'admin_u/editproduct.html', context)


def deleteItem(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    data = {
        "products": Product.objects.all(),
    }
    return render(request, 'admin_u/productlist.html', data)


def addproduct(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        data = {
            "products": Product.objects.all(),
        }
        return render(request, 'admin_u/productlist.html', data)
    context = {'form': form}
    return render(request, 'admin_u/addproduct.html', context)


def saleslist(request):
    data = {
        "transfers": Transfers.objects.all(),
    }
    return render(request, 'admin_u/saleslist.html', data)


def editTransfer(request, pk):
    transfer = Transfers.objects.get(pk=pk)
    form = TransferForm(request.POST or None, instance=transfer)
    if form.is_valid():
        form.save()
        data = {
            "transfer": Transfers.objects.all(),
        }
        return render(request, 'admin_u/saleslist.html', data)
    context = {'form': form, 'transfer': transfer}
    return render(request, 'admin_u/edittransfer.html', context)


def deleteTransfer(request, pk):
    transfer = Transfers.objects.get(pk=pk)
    transfer.delete()
    data = {
        "transfers": Transfers.objects.all(),
    }
    return render(request, 'admin_u/saleslist.html', data)


def purchaselist(request):
    data = {
        "purchases": Purchases.objects.all(),
    }
    return render(request, 'admin_u/purchaselist.html', data)


def deletePurchase(request, pk):
    purchase = Purchases.objects.get(pk=pk)
    purchase.delete()
    data = {
        "purchases": Purchases.objects.all(),
    }
    return render(request, 'admin_u/purchaselist.html', data)


def addpurchase(request):
    form = PurchasesForm(request.POST or None)
    if form.is_valid():
        form.save()
        data = {
            "purchases": Purchases.objects.all(),
        }
        return render(request, 'admin_u/purchaselist.html', data)
    context = {'form': form}
    return render(request, 'admin_u/addpurchase.html', context)


def expenselist(request):
    data = {
        "expenses": Expense.objects.all(),
    }
    return render(request, 'admin_u/expenselist.html', data)


def editexpense(request, pk):
    expense = Expense.objects.get(pk=pk)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        data = {
            "expenses": Expense.objects.all(),
        }
        return render(request, 'admin_u/expenselist.html', data)
    context = {'form': form, 'expense': expense}
    return render(request, 'admin_u/editexpense.html', context)


def deleteExpense(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.delete()
    data = {
        "expenses": Expense.objects.all(),
    }
    return render(request, 'admin_u/expenselist.html', data)


def createexpense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        form.save()
        data = {
            "expenses": Expense.objects.all()
        }
        return render(request, 'admin_u/expenselist.html', data)
    context = {'form': form}
    return render(request, 'admin_u/createexpense.html', context)


def supplierlist(request):
    data = {
        "suppliers": Supplier.objects.all(),
    }
    return render(request, 'admin_u/supplierlist.html', data)


def editSupplier(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    form = SupplierForm(request.POST or None, instance=supplier)
    if form.is_valid():
        form.save()
        data = {
            "suppliers": Supplier.objects.all(),
        }
        return render(request, 'admin_u/supplierlist.html', data)
    context = {'form': form, 'supplier': supplier}
    return render(request, 'admin_u/editsupplier.html', context)


def deleteSupplier(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    supplier.delete()
    data = {
        "suppliers": Supplier.objects.all(),
    }
    return render(request, 'admin_u/supplierlist.html', data)


def addsupplier(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        data = {
            "suppliers": Supplier.objects.all(),
        }
        return render(request, 'admin_u/supplierlist.html', data)
    context = {'form': form}
    return render(request, 'admin_u/addsupplier.html', context)


def userlist(request):
    data = {
        "users": User_Data.objects.all(),
    }
    return render(request, 'admin_u/userlist.html', data)


def adduser(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        data = {
            "users": User_Data.objects.all(),
        }
        return render(request, 'admin_u/userlist.html', data)
    context = {'form': form}
    return render(request, 'admin_u/adduser.html', context)


def editUser(request, pk):
    user = User_Data.objects.get(pk=pk)
    form = RegisterForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        data = {
            "users": User_Data.objects.all(),
        }
        return render(request, 'admin_u/userlist.html', data)
    context = {'form': form, 'user': user}
    return render(request, 'admin_u/edituser.html', context)


def deleteUser(request, pk):
    user = User_Data.objects.get(pk=pk)
    user.delete()
    data = {
        "users": User_Data.objects.all(),
    }
    return render(request, 'admin_u/userlist.html', data)


def purchasereport(request):
    data = {
        "purchases": Purchases.objects.all(),
    }
    return render(request, 'admin_u/purchasereport.html', data)


def salesreport(request):
    data = {
        "transfers": Transfers.objects.all(),
    }
    return render(request, 'admin_u/salesreport.html', data)


def inventoryreport(request):
    data = {
        "products": Product.objects.all(),
    }
    return render(request, 'admin_u/inventoryreport.html', data)


def purchaseorderreport(request):
    data = {
        "expenses": Expense.objects.all(),
    }
    return render(request, 'admin_u/purchaseorderreport.html', data)


def chart_apex(request):
    ranges = ['2022-01-01','2022-01-31','2022-02-01','2022-02-28','2022-03-01','2022-03-31','2022-04-01','2022-04-30',
              '2022-05-01','2022-05-31','2022-06-01','2022-06-30','2022-07-01','2022-07-01','2022-08-01','2022-08-31',
              '2022-09-01','2022-09-30','2022-10-01','2022-10-31','2022-11-01','2022-11-30','2022-12-01','2022-12-31',]
    slinedata = {
        'jan': Transfers.objects.filter(start_of_loan__range=[ranges[0],ranges[1]]).count(),
        'feb': Transfers.objects.filter(start_of_loan__range=[ranges[2],ranges[3]]).count(),
        'mar': Transfers.objects.filter(start_of_loan__range=[ranges[4],ranges[5]]).count(),
        'apr': Transfers.objects.filter(start_of_loan__range=[ranges[6],ranges[7]]).count(),
        'may': Transfers.objects.filter(start_of_loan__range=[ranges[8],ranges[9]]).count(),
        'jun': Transfers.objects.filter(start_of_loan__range=[ranges[10],ranges[11]]).count(),
        'july': Transfers.objects.filter(start_of_loan__range=[ranges[12],ranges[13]]).count(),
        'aug': Transfers.objects.filter(start_of_loan__range=[ranges[14],ranges[15]]).count(),
        'sep': Transfers.objects.filter(start_of_loan__range=[ranges[16],ranges[17]]).count(),
        'oct': Transfers.objects.filter(start_of_loan__range=[ranges[18],ranges[19]]).count(),
        'nov': Transfers.objects.filter(start_of_loan__range=[ranges[20],ranges[21]]).count(),
        'dec': Transfers.objects.filter(start_of_loan__range=[ranges[22],ranges[23]]).count(),
    }
    return render(request, 'admin_u/chart-apex.html', slinedata)


# student views

def indexs(request):
    date = datetime.now()
    data = {
        'users_num': len(User_Data.objects.all()),
        'returned_items': len(Transfers.objects.filter(Q(status='Returned')).values()),
        'budget': Finance.objects.all(),
        'total_purchase': Finance.objects.all(),
        'purchase_items': len(Purchases.objects.all()),
        'transfers': len(Transfers.objects.all()),
        "products": Product.objects.filter(Q(adding_date=date)).values(),
        'transfersp': Transfers.objects.filter(Q(start_of_loan=date) | Q(end_of_loan=date)).values(),
    }
    return render(request, 'student/index.html', data)


def productlists(request):
    data = {
        "products": Product.objects.all(),
    }
    return render(request, 'student/productlist.html', data)


def addproducts(request):
    return render(request, 'student/addproduct.html')


def saleslists(request):
    return render(request, 'student/saleslist.html')


def purchaselists(request):
    return render(request, 'student/purchaselist.html')


def quotationlists(request):
    return render(request, 'admin_u/quotationlist.html')


def addquotations(request):
    return render(request, 'student/addquotation.html')


def supplierlists(request):
    return render(request, 'student/supplierlist.html')


def userlists(request):
    return render(request, 'student/userlist.html')


def purchasereports(request):
    data = {
        "purchases": Purchases.objects.all(),
    }
    return render(request, 'student/purchasereport.html', data)


def salesreports(request):
    data = {
        "transfers": Transfers.objects.all(),
    }
    return render(request, 'student/salesreport.html', data)


def inventoryreports(request):
    data = {
        "products": Product.objects.all(),
    }
    return render(request, 'admin_u/inventoryreport.html', data)


def purchaseorderreports(request):
    data = {
        "expenses": Expense.objects.all(),
    }
    return render(request, 'admin_u/purchaseorderreport.html', data)



def chart_apexs(request):
    return render(request, 'student/chart-apex.html')


# teacher views

def indext(request):
    date = datetime.now()
    data = {
        'users_num': len(User_Data.objects.all()),
        'returned_items': len(Transfers.objects.filter(Q(status='Returned')).values()),
        'budget': Finance.objects.all(),
        'total_purchase': Finance.objects.all(),
        'purchase_items': len(Purchases.objects.all()),
        'transfers': len(Transfers.objects.all()),
        "products": Product.objects.filter(Q(adding_date=date)).values(),
        'transfersp': Transfers.objects.filter(Q(start_of_loan=date) | Q(end_of_loan=date)).values(),
    }
    return render(request, 'teacher/index.html', data)


def productlistt(request):
    data = {
        "products": Product.objects.all(),
    }
    return render(request, 'teacher/productlist.html', data)


def saleslistt(request):
    return render(request, 'teacher/saleslist.html')


def purchaselistt(request):
    return render(request, 'teacher/purchaselist.html')


def expenselistt(request):
    return render(request, 'teacher/expenselist.html')


def quotationlistt(request):
    return render(request, 'teacher/quotationlist.html')


def addquotationt(request):
    return render(request, 'teacher/addquotation.html')


def supplierlistt(request):
    return render(request, 'teacher/supplierlist.html')


def userlistt(request):
    return render(request, 'teacher/userlist.html')


def purchasereportt(request):
    return render(request, 'teacher/purchasereport.html')


def salesreportt(request):
    return render(request, 'teacher/salesreport.html')


def inventoryreportt(request):
    return render(request, 'teacher/inventoryreport.html')


def purchaseorderreportt(request):
    return render(request, 'teacher/purchaseorderreport.html')


def chart_apext(request):
    return render(request, 'teacher/chart-apex.html')


def addusert(request):
    return render(request, 'teacher/adduser.html')
