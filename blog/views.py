from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Info, Product, Boiler, Onsugi, Aircon, Consult
from django.http import HttpResponse
import json
import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

# class PostLV(ListView):
#     model = Post
#     context_object_name = 'post_list'
#
# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post_detail.html', {'post':post})


def first(request):
    # popup = Popup.objects.all()
    return render(request, 'blog/service.html', {'check':1})

def index(request):
    # consult와 연결
    if request.method == 'POST':
        form = request.POST
        new_model = Consult(name=form["name"], phone=form["phone"], content=form["content"], time=datetime.datetime.today())
        new_model.save()


    return render(request, 'blog/index.html')


def service(request):
    if request.method == 'POST':
        print("aaaaaa")
        form = request.POST
        if form['product_type'] == 'boiler' :
            model = Boiler.objects.all()
            return render(request, 'blog/service_boiler.html', {'model':model})
        elif form['product_type'] == 'onsugi' :
            model = Onsugi.objects.all()
            return render(request, 'blog/service_onsugi.html', {'model':model})
        elif form['product_type'] == 'aircon' :
            model = Aircon.objects.all()
            return render(request, 'blog/service_aircon.html', {'model':model})

    else:
        return render(request, 'blog/service.html')

def service_popup(request):
    return render(request, 'blog/service_popup.html')



def service_boiler(request):
    if request.method == 'POST':
        form = request.POST
        print(form)

        try:
            if form['product_type'] == 'boiler':
                model = Boiler.objects.all()
                return render(request, 'blog/service_boiler.html', {'model':model})


        except:
            if form['pyeong'] != '' and form['grade'] == '':
                try:
                    print("Asdsadsad")
                    model = Boiler.objects.filter(pyeong=form['pyeong'])
                    # print(model1.values())
                    # print(type(list(model1)))
                    tmp_list = []
                    for i in model.values():
                        tmp_list.append(i)
                    print(tmp_list)
                    return HttpResponse(json.dumps(tmp_list, ensure_ascii=False))
                except:
                    model = Boiler.objects.all()
                    return render(request, 'blog/service_boiler.html', {'model': model})
                # return render(request, 'blog/service.html', {'model': model})



            elif form['pyeong'] == '' and form['grade'] == '' :
                model = Boiler.objects.all()
                return render(request, 'blog/service_boiler.html', {'model': model})

            elif form['pyeong'] != ''  and form['grade'] != '':
                rows = Boiler.objects.filter(pyeong=form['pyeong'], grade=form['grade'])
                model = Boiler.objects.all()
                return render(request, 'blog/service_boiler.html', {'model': model, 'rows': rows})
            else:
                model = Boiler.objects.all()
                return render(request, 'blog/service_boiler.html', {'model': model})



def service_onsugi(request):
    if request.method == 'POST':
        form = request.POST
        print(form)

        try:
            if form['product_type'] == 'onsugi':
                model = Onsugi.objects.all()
                return render(request, 'blog/service_onsugi.html', {'model':model})


        except:
            if form['capacity'] != '' and form['fuel'] == '':
                try:
                    print("Asdsadsad")
                    model = Onsugi.objects.filter(capacity=form['capacity'])
                    tmp_list = []
                    for i in model.values():
                        tmp_list.append(i)
                    print(tmp_list)
                    return HttpResponse(json.dumps(tmp_list, ensure_ascii=False))
                except:
                    model = Onsugi.objects.all()
                    return render(request, 'blog/service_onsugi.html', {'model': model})
                # return render(request, 'blog/service.html', {'model': model})



            elif form['capacity'] == '' and form['fuel'] == '' :
                model = Onsugi.objects.all()
                return render(request, 'blog/service_onsugi.html', {'model': model})

            elif form['capacity'] != ''  and form['fuel'] != '':
                rows = Onsugi.objects.filter(capacity=form['capacity'], fuel=form['fuel'])
                model = Onsugi.objects.all()
                return render(request, 'blog/service_onsugi.html', {'model': model, 'rows': rows})


            else:
                model = Onsugi.objects.all()
                return render(request, 'blog/service_onsugi.html', {'model': model})


def service_aircon(request):
    if request.method == 'POST':
        form = request.POST
        print(form)

        try:
            if form['product_type'] == 'aircon':
                model = Aircon.objects.all()
                return render(request, 'blog/service_aircon.html', {'model':model})


        except:
            if form['service_type'] != '' and form['aircon_type'] == '':
                try:
                    model = Aircon.objects.filter(service_type=form['service_type'])
                    tmp_list = []
                    for i in model.values():
                        tmp_list.append(i)
                    print(tmp_list)
                    return HttpResponse(json.dumps(tmp_list, ensure_ascii=False))
                except:
                    model = Aircon.objects.all()
                    return render(request, 'blog/service_aircon.html', {'model': model})
                # return render(request, 'blog/service.html', {'model': model})

            elif form['service_type'] != '' and form['aircon_type'] != '' and form['company'] == '':
                try:
                    model = Aircon.objects.filter(service_type=form['service_type'], aircon_type=form['aircon_type'])
                    tmp_list = []
                    for i in model.values():
                        tmp_list.append(i)
                    print(tmp_list)
                    return HttpResponse(json.dumps(tmp_list, ensure_ascii=False))
                except:
                    model = Aircon.objects.all()
                    return render(request, 'blog/service_aircon.html', {'model': model})
                # return render(request, 'blog/service.html', {'model': model})


            elif form['service_type'] != '' and form['aircon_type'] != '' and form['company'] != '' and form['structure'] == '':
                try:
                    model = Aircon.objects.filter(service_type=form['service_type'], aircon_type=form['aircon_type'], company=form['company'])
                    tmp_list = []
                    for i in model.values():
                        tmp_list.append(i)
                    print(tmp_list)
                    return HttpResponse(json.dumps(tmp_list, ensure_ascii=False))
                except:
                    model = Aircon.objects.all()
                    return render(request, 'blog/service_aircon.html', {'model': model})



            elif form['service_type'] == '' and form['aircon_type'] == '' and form['company'] == '' and form['structure'] == '' :
                model = Aircon.objects.all()
                return render(request, 'blog/service_aircon.html', {'model': model})

            elif form['service_type'] != '' and form['aircon_type'] != '' and form['company'] != '' and form['structure'] != '':
                rows = Aircon.objects.filter(service_type=form['service_type'], aircon_type=form['aircon_type'], company=form['company'], structure=form['structure'])
                model = Aircon.objects.all()
                return render(request, 'blog/service_aircon.html', {'model': model, 'rows': rows})

            else:
                model = Aircon.objects.all()
                return render(request, 'blog/service_aircon.html', {'model': model})

def daesung_info(request):
    return render(request, 'blog/daesung_info.html')

def navien_info(request):
    return render(request, 'blog/navien_info.html')

def kiturami_info(request):
    return render(request, 'blog/kiturami_info.html')

def rinnai_info(request):
    return render(request, 'blog/rinnai_info.html')


def product_info(request):
    return render(request, 'blog/product_info.html')

def consult(request):
    model = Consult.objects.all().order_by('-id')
    paginator = Paginator(model, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/consult.html', {'model': posts})

def consult_content(request):
    req = request.GET
    print([req['id']])
    model = Consult.objects.filter(id=req['id'])
    return render(request, 'blog/consult_content.html', {'model': model})

def recent(request):
    return render(request, 'blog/recent.html')

def customer(request):
    return render(request, 'blog/customer.html')

def map_1(request):
    return render(request, 'blog/map.html')






