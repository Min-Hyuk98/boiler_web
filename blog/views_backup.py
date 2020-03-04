from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Info, Product, Boiler, Onsugi, Aircon
from django.http import HttpResponse
import json
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
    return render(request, 'blog/index.html')


def service(request):

    if request.method == 'POST':
        form = request.POST
        print(form)
        # pyeong = form['pyeong']
        # product_type = form['product_type']
        # p_type = form['p_type']
        # product_name = form['product_name']

        if form['pyeong'] != '' and form['p_type'] == '':
            try:
                model = Product.objects.filter(pyeong=form['pyeong'])
                # print(model1.values())
                # print(type(list(model1)))
                tmp_list = []
                for i in model.values():
                    tmp_list.append(i)
                print(tmp_list)
                return HttpResponse(json.dumps(tmp_list, ensure_ascii=False))
            except:
                model = Product.objects.all()
                return render(request, 'blog/service.html', {'model': model})
            # return render(request, 'blog/service.html', {'model': model})

        elif form['pyeong'] != '' and form['p_type'] != '' and form['p_type2'] == '':
            try:
                model = Product.objects.filter(pyeong=form['pyeong'], p_type=form['p_type'])
                print(model)
                tmp_list = []
                for i in model.values():
                    tmp_list.append(i)
                print(tmp_list)
                return HttpResponse(json.dumps(tmp_list, ensure_ascii=False))
            except:
                model = Product.objects.all()
                return render(request, 'blog/service.html', {'model': model})
            # return render(request, 'blog/service.html', {'model2': model})

        elif form['pyeong'] != '' and form['p_type'] != '' and form['p_type2'] != '' and form['grade'] == '':
            try:
                model = Product.objects.filter(pyeong=form['pyeong'], p_type=form['p_type'], p_type2=form['p_type2'])
                print(model)
                tmp_list = []
                for i in model.values():
                    tmp_list.append(i)
                print(tmp_list)
                return HttpResponse(json.dumps(tmp_list, ensure_ascii=False))
            except:
                model = Product.objects.all()
                return render(request, 'blog/service.html', {'model': model})
            # return render(request, 'blog/service.html', {'model3': model})

        elif form['pyeong'] != '' and form['p_type'] != '' and form['p_type2'] != '' and form['grade'] != '':
            model = Product.objects.all()
            rows = Product.objects.filter(pyeong=form['pyeong'], p_type=form['p_type'], p_type2=form['p_type2'], grade=form['grade'])
            return render(request, 'blog/service.html', {'model': model, 'rows':rows})

        elif form['pyeong'] == '' and form['p_type'] == '' and form['p_type2'] == '' and form['grade'] == '':
            model = Product.objects.all()
            return render(request, 'blog/service.html', {'model': model})

    else:
        model = Product.objects.all()
        return render(request, 'blog/service.html', {'model': model})




