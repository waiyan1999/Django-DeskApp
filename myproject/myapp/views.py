from django.shortcuts import render,redirect,HttpResponse
from myapp.models import Product
from myapp.form import productUploadForm,productEditForm

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request,'index.html')

def product(request):
    p_obj = Product.objects.all()
    fm = productUploadForm()
    context = {'p_obj': p_obj,'fm':fm}
    
    
    if request.method == 'POST':
        fm = productUploadForm(request.POST, request.FILES)
        if fm.is_valid():
            
            fm.save()
            print('Data Successfully Saved')
            return redirect('product')
            
        else:
            print("Error Occur")
            return redirect('uploadpro')
            
            
    
    return render(request,'product.html',context)

def loginView(request):
    return render(request,'login.html')

def registerView(request):
    return render(request,'register.html')

def productDetail(request,id):
    p_detail = Product.objects.filter(id=id)
    fm = productEditForm()
    context = {'p_detail': p_detail, 'fm':fm }
    
    # if request.method.get('p_edit') == 'p_edit':
    
    if request.method == "POST":
        fm = productEditForm(request.POST, request.FILES , instance= p_detail)
        if fm.is_valid():
            fm.save()
            print(request.POST)
            print(" Successful Update Data")
            
            
        else:
            print(request.POST)
            print(" Error Edit")
            
        
        return redirect('porduct')
        
        
    return render(request,'product-detail.html',context)


def deleteProduct(request,id):
    p_delete = Product.objects.filter(id=id)
    p_delete.delete()
    print('Delete Successful')
    return redirect('product')

def editProduct(request,id):
    p_edit = Product.objects.get(id=id)
    fm = productEditForm()
    context = {'fm':fm ,'p_edit': p_edit}
    
    if request.method == 'POST':
        fm = productEditForm(request.POST,request.FILES,instance=p_edit)
        if fm.is_valid():
            fm.save()
            print(request.POST)
            print("Edit Successfully")
            return redirect('product')
            
        else:
            print(request.POST)
            print("Edit Error")
            return redirect('editproduct')
        
    return render(request,'product-edit.html',context)  


def listProduct(request):
    p_list = Product.objects.all()
    context = {'p_list':p_list}
    return render(request, 'product-list.html', context)
            
    