from app.models import OSPaperInfo


def add_os_paper(stu_name, src, paper_name):
    exist_info = OSPaperInfo.objects.filter(stu_name=stu_name)
    if exist_info.count() > 0:
        exist_info.update(paper_name=paper_name, src=src, stu_name=stu_name)
        return True
    else:
        OSPaperInfo(paper_name=paper_name, src=src, stu_name=stu_name).save()
        return False
