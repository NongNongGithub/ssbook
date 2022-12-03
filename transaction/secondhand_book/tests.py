# -*- coding: gbk -*-
from django.test import TestCase
from secondhand_book.models import *
# Create your tests here.

# UserInfo:
# UserID = models.AutoField(primary_key=True)
# Username = models.CharField(max_length=20)
# password = models.CharField(max_length=20)
# Email = models.EmailField(max_length=30)

# Goods:
# Commodity_ID = models.AutoField(primary_key=True)
# Price = models.IntegerField()
# Contact_QQ = models.DecimalField(max_digits=11, decimal_places=0)
# Note = models.CharField(max_length=120)
# Date = models.DateTimeField(auto_now=False, auto_now_add=True)
# UserID = models.ForeignKey('UserInfo', related_name='UserID_Goods', on_delete=models.CASCADE)
# Commodity_Name = models.CharField(max_length=120, null=True, blank=True)
if __name__ == '__main__':
    # UserInfo.objects.create(
    #     Username='楹婚様', password='123456', Email='765019392@qq.com')
    # q = UserInfo.objects.filter(Username='楹婚様')
    # newImg = str(q[0].UserID) + '.jpg'
    # q.update(Img=newImg)

    Goods.objects.create(price=25, user_contact='765019392',
                         user_id='1234', commodity_name='高等数学', picture='img/Math.webp')
    # q = Goods.objects.filter(commodity_name='楂樼瓑鏁板')

    # UserInfo.objects.create(Username='鍒樺繝涓?',
    #                         password='123456', Email='2328954508@qq.com')
    # q = UserInfo.objects.filter(Username='鍒樺繝涓?')
    # newImg = str(q[0].UserID) + '.jpg'
    # q.update(Img=newImg)
