from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from app1.forms.add import AddForm
from app1.models.product import Product

def index(request):
	return HttpResponse('')

def add(request):
	form = AddForm()

	if request.method == 'POST':
		form = AddForm(request.POST)
		status = 1 if request.POST.get('status', 0) == 'on' else 0
		if form.is_valid():
			p = Product(name=request.POST.get('name'), status=status)
			p.save()
			return redirect('/')

	return render(request, 'add.html', {'form':form, 'title':'Add product'}, content_type='text/html', status=201)

def edit(request):
	id = request.GET.get('id', 0)
	try:
		p = Product.objects.get(id=id.strip())
		if request.method == 'POST':
			status = 1 if request.POST.get('status', 0) == 'on' else 0
			form = AddForm(request.POST)
			if form.is_valid():
				p.name = request.POST.get('name').strip()
				p.status = status
				p.save()
				return redirect('/')
		else:
			form = AddForm({'name':p.name, 'status':p.status})
	except Exception as e:
		return HttpResponse("Errors", status=500)
	return render(request, 'add.html', {'form':form, 'title':'Edit product'}, content_type='text/html')

def del_product(request):
	id = request.GET.get('id', 0)
	try:
		p = Product.objects.get(id=id.strip())
		p.delete()
	except Exception as e:
		return HttpResponse("Errors", status=500)
	return redirect('/')

def list(request):
	p=Product.objects.all()
	return render(request, 'list.html', {'products':p}, content_type='text/html')