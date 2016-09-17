from app.models import OSPaperInfo


def add_os_paper(stu_name, src, paper_name):
    exist_info = OSPaperInfo.objects.filter(stu_name=stu_name)
    paper_info = OSPaperInfo.objects.filter(paper_name=paper_name)
    if paper_info.count() > 0:
        res = [paper_item.stu_name for paper_item in paper_info]
        res_str = "选了同一篇文章的人："
        for paper_item in paper_info:
            res_str += paper_item.stu_name + " "
        res_str += "<br/> 你们选的文章是：" + paper_name
    else:
        res_str = None
    if exist_info.count() > 0:
        exist_info.update(paper_name=paper_name, src=src, stu_name=stu_name)
        ret = True
    else:
        OSPaperInfo(paper_name=paper_name, src=src, stu_name=stu_name).save()
        ret = False
    return ret, res_str
