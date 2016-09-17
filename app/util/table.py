import xlwt
from django.http import HttpResponse

from app.models import OSPaperInfo


def dataset2xls(dataset, xls_name, column_names):
    wb = xlwt.Workbook()
    ws = wb.add_sheet(xls_name)
    style_title = xlwt.easyxf('font: bold on,colour_index green;')
    for i, column_name in enumerate(column_names):
        ws.write(0, i, column_name, style_title)
    for i, data_row in enumerate(dataset):
        for j, data in enumerate(data_row):
            ws.write(i + 1, j, data)
    wb.save(xls_name + '.xls')
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment;filename="%s.xls"' % xls_name
    wb.save(response)
    return response


def test2xls():
    os_paper_info = OSPaperInfo.objects.all()
    os_paper_info_dataset = [
        [info.stu_name, info.paper_name, 'osdi2014' if info.src == 0 else (
            'sosp2015' if info.src == 1 else 'osdi2016')] for info in os_paper_info]
    return dataset2xls(os_paper_info_dataset, 'paper', ['姓名', '论文名', '来源'])
