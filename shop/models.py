from django.db import models
from django.utils import timezone

from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator



class Pattern(models.Model):

    class Meta:
        db_table = "pattern"

    title   = models.CharField(verbose_name="タイトル",max_length=30)
    dt      = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    img     = models.ImageField(verbose_name="画像",upload_to="shop/pattern/")

    #TODO:ここに糸の太さを指定するフィールドを追加。糸の太さは1つしかないからPatternModelに記録。
    size    = models.IntegerField(verbose_name="糸の太さ",default=1,validators=[MinValueValidator(1),MaxValueValidator(10)])

    def __str__(self):
        return self.title

class PatternRecipe(models.Model):

    #TODO:Patternモデルクラスと1対多のリレーションを作る。
    target      = models.ForeignKey(Pattern,verbose_name="対象の模様",on_delete=models.CASCADE)

    #TODO:colorフィールドは16進数カラーコードの正規表現を指定し、それのみ受け付ける
    #参照:https://noauto-nolife.com/post/django-models-regex-validate/
    color_regex = RegexValidator(regex=r'^#(?:[0-9a-fA-F]{6})$')
    color       = models.CharField(verbose_name="色",max_length=7,validators=[color_regex],default="#000000")

    number      = models.IntegerField(verbose_name="本数",default=1,validators=[MinValueValidator(1),MaxValueValidator(10)])



class Contact(models.Model):

    dt      = models.DateTimeField(verbose_name="お問い合わせ日時",default=timezone.now)
    subject = models.CharField(verbose_name="お問い合わせ件名",max_length=100)
    content = models.CharField(verbose_name="お問い合わせ内容",max_length=1000)

    def __str__(self):
        return self.subject



