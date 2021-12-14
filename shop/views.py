from django.shortcuts import render,redirect
from django.views import View

from django.http.response import JsonResponse

from .models import Pattern
from .forms import PatternForm,PatternRecipeForm


class IndexView(View):

    def get(self, request, *args, **kwargs):

        patterns    = Pattern.objects.all()
        context     = { "patterns":patterns }

        return render(request,"shop/index.html",context)

index   = IndexView.as_view()


class PatternView(View):

    def get(self, request, *args, **kwargs):

        patterns    = Pattern.objects.order_by("-dt")
        context     = { "patterns":patterns }

        return render(request,"shop/pattern.html",context)

pattern = PatternView.as_view()


class PatternModView(View):

    def get(self, request, *args, **kwargs):

        #TODO:ここに模様のフォームをレンダリング

        return render(request,"shop/pattern_mod.html")

    def post(self, request, *args, **kwargs):
        #模様の保存処理

        json    = { "error":True }
        form    = PatternForm(request.POST, request.FILES)

        print(request.POST)
        
        if not form.is_valid():
            print("バリデーションNG")
            return JsonResponse(json)

        print("バリデーションOK")


        #TODO:保存するとき、保存したモデルオブジェクトのIDを入手。レシピ登録時に使う。
        pattern = form.save()
        target  = pattern.id



        #TODO:まずcolorとnumberがあるかチェック。なければNG
        if "color" not in request.POST or "number" not in request.POST:
            print("バリデーションNG")
            return JsonResponse(json)

        #TODO:colorとnumberはそれぞれリスト型なので、.getlist()メソッドを使って呼び出しする。普通にrequest.POST["color"]とすると、得られる値はひとつだけ。
        print(request.POST.getlist("color"))
        print(request.POST.getlist("number"))


        #TODO:colorとnumberがリストではない場合はNG
        if type(request.POST.getlist("color")) is not list and type(request.POST.getlist("number")) is not list:
            print("バリデーションNG")
            return JsonResponse(json)


        colors  = request.POST.getlist("color")
        numbers = request.POST.getlist("number")

        for ( color, number ) in zip( colors, numbers ):
            dic             = {}
            dic["color"]    = color
            dic["number"]   = number
            dic["target"]   = target

            print(dic)
            
            form    = PatternRecipeForm(dic)

            if not form.is_valid():
                print("レシピバリデーションNG")

            print("レシピバリデーションOK")
            form.save()

        json["error"]   = False


        return JsonResponse(json)

pattern_mod = PatternModView.as_view()











#お問い合わせのビュー
class ContactView(View):

    def get(self, request, *args, **kwargs):
        #TODO:ここでお問い合わせフォームのHTMLをレンダリング
        pass

    def post(self, request, *args, **kwargs):
        #TODO:ここでお問い合わせを受けて、管理者にメール送信
        pass

contact = ContactView.as_view()

