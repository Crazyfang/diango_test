# encoding:utf-8

from django.http import HttpResponse
from people.models import People


def testdb(request):
    example = People(name='方勇', age=22)
    example.save()
    return HttpResponse('<p>数据插入成功!</p>')


# 数据库操作
def get(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = People.objects.all()

    # 输出所有数据
    for var in list:
        response1 += ("{}-----{}".format(var.name, var.age))
    response = response1
    return HttpResponse("<p>" + response + "</p>")
