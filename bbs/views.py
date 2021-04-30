from django.shortcuts import render,redirect
from django.views import View

from .models import Topic
from .forms import TopicForm

class BbsView(View):

    def get(self, request, *args, **kwargs):

        topics = Topic.objects.all()

        if "search" in request.GET:
            print(request.GET["search"])

        chobos = [
            {"id": "0", "title": "現金", "price": "3000"},
            {"id": "1", "title": "受取手形", "price": "3000"},
            {"id": "2", "title": "売上金額", "price": "3000"},
            {"id": "3", "title": "会議費", "price": "3000"},
            {"id": "4", "title": "仕入価格", "price": "3000"},
            {"id": "5", "title": "研究開発費", "price": "3000"},
            {"id": "6", "title": "福利厚生費", "price": "3000"},
            {"id": "7", "title": "家賃", "price": "3000"},
            {"id": "8", "title": "広告宣伝費", "price": "3000"},
            {"id": "9", "title": "通信費", "price": "3000"},
            {"id": "A", "title": "交通費", "price": "3000"},
            {"id": "B", "title": "接待交際費", "price": "3000"},
            {"id": "C", "title": "消費税", "price": "3000"},
            {"id": "D", "title": "印税", "price": "3000"},
            {"id": "E", "title": "法人税", "price": "3000"},
            {"id": "F", "title": "残高", "price": "3000"},
        ]
        context = {"chobos":chobos,
                   "topics":topics}

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        """
        if "comment" in request.POST:
             posted = Topic( comment = request.POST["comment"])
             posted.save()
             print(request.POST["comment"])
        """

        #forms.pyによるバリデーションを行う
        form = TopicForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")

        return redirect("bbs:index")

index   = BbsView.as_view()




class BbsDeleteView(View):
    def post(self, request, pk, *args, **kwargs):

        topic = Topic.objects.filter(id=pk).first()
        topic.delete()

        return redirect("bbs:index")

delete  = BbsDeleteView.as_view()
