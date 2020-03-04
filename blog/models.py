from django.db import models
import datetime

# Create your models here.
class Info(models.Model):
    pyeong = models.IntegerField("평형") #26, 32, 40, 50, 60
    product_type = models.CharField("종류", max_length=100) #대성셀틱, 경동나비엔, 귀뚜라미, 린나이
    p_type = models.CharField("소종류", max_length=100) #보일러, 온수기, 온도조절기, 온수매트
    product_name = models.CharField("제품명", max_length=100)
    price = models. IntegerField("가격")

    def __str__(self):
        return self.product_name


class Product(models.Model):
    pyeong = models.IntegerField("평형") #26, 32, 40, 50, 60
    product_type= models.CharField("제조사", max_length=100) #대성셀틱, 경동나비엔, 귀뚜라미, 린나이
    p_type = models.CharField("제품종류", max_length=100) #보일러, 온수기, 온도조절기, 온수매트
    p_type2 = models.CharField("제품종류2", max_length=100, blank=True)  # 전기보일러, 가스온수기, 온도조절기, 온수매트
    grade = models.CharField("제품등급", max_length=100)
    product_name = models.CharField("제품명", max_length=100)
    price = models. IntegerField("가격")
    image_url = models.URLField("이미지", max_length=100, blank=True)
    image1 = models.CharField("이미지1", max_length=100, blank=True)
    image2 = models.CharField("이미지2", max_length=100, blank=True)
    image3 = models.CharField("이미지3", max_length=100, blank=True)


    p1 = models.CharField("p1", max_length=100, blank=True)
    p2 = models.CharField("p2", max_length=100, blank=True)
    p3 = models.CharField("p3", max_length=100, blank=True)
    p4 = models.CharField("p4", max_length=100, blank=True)
    p5 = models.CharField("p5", max_length=100, blank=True)
    p6 = models.CharField("p6", max_length=100, blank=True)
    p7 = models.CharField("p7", max_length=100, blank=True)

    i1 = models.IntegerField("i1", blank=True, null=True)
    i2 = models.IntegerField("i2", blank=True, null=True)
    i3 = models.IntegerField("i3", blank=True, null=True)
    i4 = models.IntegerField("i4", blank=True, null=True)
    i5 = models.IntegerField("i5", blank=True, null=True)
    i6 = models.IntegerField("i6", blank=True, null=True)

    def __str__(self):
        return self.product_name

class Boiler(models.Model):
    product_type = models.CharField("종류", max_length=100) #보일러, 온수기, 에어컨
    pyeong = models.IntegerField("평형")  # 26, 32, 40, 50, 60
    grade = models.CharField("사양", max_length=100)
    product_name = models.CharField("제품명", max_length=100)
    price = models.IntegerField("가격")


    p1 = models.CharField("p1", max_length=100, blank=True)
    p2 = models.CharField("p2", max_length=100, blank=True)
    p3 = models.CharField("p3", max_length=100, blank=True)
    p4 = models.CharField("p4", max_length=100, blank=True)

    i1 = models.IntegerField("i1", blank=True, null=True)
    i2 = models.IntegerField("i2", blank=True, null=True)
    i3 = models.IntegerField("i3", blank=True, null=True)

    def __str__(self):
        return repr(self.product_name) + "  /  " + repr(self.pyeong) + "  /  " + repr(self.grade)

class Onsugi(models.Model):
    product_type = models.CharField("종류", max_length=100)  # 보일러, 온수기, 에어컨
    capacity = models.IntegerField("용량")  # 15, 30, 50
    fuel = models.CharField("사용연료", max_length=100) #전기, 가스
    product_name = models.CharField("제품명", max_length=100)
    price = models.IntegerField("가격")


    p1 = models.CharField("p1", max_length=100, blank=True)
    p2 = models.CharField("p2", max_length=100, blank=True)
    p3 = models.CharField("p3", max_length=100, blank=True)
    p4 = models.CharField("p4", max_length=100, blank=True)

    i1 = models.IntegerField("i1", blank=True, null=True)
    i2 = models.IntegerField("i2", blank=True, null=True)
    i3 = models.IntegerField("i3", blank=True, null=True)

    def __str__(self):
        return repr(self.product_name) + "  /  " + repr(self.capacity) + "  /  " + repr(self.fuel)

class Aircon(models.Model):
    product_type = models.CharField("종류", max_length=100)  # 보일러, 온수기, 에어컨
    service_type = models.CharField("서비스종류", max_length=100) #이전설치, 신규설치, 냉매가스충전, 누수
    aircon_type = models.CharField("에어컨종류", max_length=100) #벽걸이, 스텐드, 스텐드벽걸이. 천장형
    company = models.CharField("제조사", max_length=100)  #삼성, 엘지, 캐리어, 위니아대우, 기타
    structure = models.CharField("배관형태", max_length=100) #매립형, 노출형, 기타
    product_name = models.CharField("제품명", max_length=100)
    price = models.IntegerField("가격")


    p1 = models.CharField("p1", max_length=100, blank=True)
    p2 = models.CharField("p2", max_length=100, blank=True)
    p3 = models.CharField("p3", max_length=100, blank=True)
    p4 = models.CharField("p4", max_length=100, blank=True)

    i1 = models.IntegerField("i1", blank=True, null=True)
    i2 = models.IntegerField("i2", blank=True, null=True)
    i3 = models.IntegerField("i3", blank=True, null=True)

    def __str__(self):
        return repr(self.product_name) + "  /  " + repr(self.service_type) + "  /  " + repr(self.aircon_type) + "  /  " + repr(self.company) + "  /  " + repr(self.structure)


class Consult(models.Model):
    name = models.CharField("name", max_length=400)
    phone = models.CharField("phone", max_length=400)
    content = models.CharField("content", max_length=400)
    time = models.DateField("time", default=datetime.datetime.today)
    reply = models.CharField("reply", max_length=400, blank=True)

    p1 = models.CharField("p1", max_length=100, blank=True)
    p2 = models.CharField("p2", max_length=100, blank=True)
    p3 = models.CharField("p3", max_length=100, blank=True)
    p4 = models.CharField("p4", max_length=100, blank=True)

    i1 = models.IntegerField("i1", blank=True, null=True)
    i2 = models.IntegerField("i2", blank=True, null=True)
    i3 = models.IntegerField("i3", blank=True, null=True)

    def __str__(self):
        a = repr(self.id)
        b = repr(self.name)
        c = repr(self.reply)
        return a + " " + b + " " + c

# class Popup(models.Model):
#     name = models.CharField(max_length=10)
#     photo = models.ImageField(upload_to="popup")
#
#     def __str__(self):
#         return repr(self.name) + " / " + repr(self.photo)