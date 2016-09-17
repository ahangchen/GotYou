from django.http import HttpResponse
from django.shortcuts import render
from app.ctrl import info


# Create your views here.
from app.util.table import test2xls


def main(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def class_os(request):
    return render(request, 'class/os.html')


def os_paper(request):
    stu_name = request.POST['stu_name']
    paper_name = request.POST['paper_name']
    paper_src = request.POST['paper_src']
    ret, res = info.add_os_paper(stu_name, paper_src, paper_name)
    if res is not None:
        return HttpResponse(res)
    if ret:
        return HttpResponse("修改成功")
    else:
        return HttpResponse("添加成功")


def get_os_result(request):
    return test2xls()
