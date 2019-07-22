from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()                       
    nickname = models.CharField(max_length=10)        
    area = models.CharField(max_length=10)
    report_count = models.IntegerField(default=0)             #신고횟수
    podo = models.IntegerField(default=10)             # 초기10알
    gender = models.BooleanField(default=False)    
    image = models.FileField(null=True, blank=True)
    #keywords = models.CharField()                      #보류


class Image(models.Model):
    images = models.ImageField() 


class Option(models.Model):
    vim = models.BooleanField(default=False)
    board = models.BooleanField(default=False)
    desk = models.BooleanField(default=False)
    multitap = models.IntegerField(default=0)
    speaker = models.BooleanField(default=False)
    lights = models.BooleanField(default=False)
    mirror = models.BooleanField(default=False)
    aircomditioner = models.BooleanField(default=False)
    printer = models.BooleanField(default=False)


class Purpose_category(models.Model):
    study = models.BooleanField(default=False)
    performance = models.BooleanField(default=False)
    practice = models.BooleanField(default=False)
    conference = models.BooleanField(default=False)
    etc = models.BooleanField(default=False)
    etc_what = models.CharField(max_length=50) #새로 만듬 어떤 목적으로 사용하는지 적을 수 있는 필드


class Date(models.Model):
    day = models.IntegerField(default=1)
    start_time = models.IntegerField(default=0)
    end_time = models.IntegerField(default=0)


class Like(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


class Review(models.Model):
    image = models.ForeignKey(Image, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(null=True)


class Qna(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirm = models.BooleanField(default=False)
    context = models.TextField()


class Post(models.Model):
    image = models.ForeignKey(Image, default=None, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(Purpose_category, default=None, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, default=None, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, default=None, on_delete=models.CASCADE)
    qna = models.ForeignKey(Qna, default=None, on_delete=models.CASCADE)            # QnA
    like =  models.ForeignKey(Like, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)                           
    updated_at = models.DateTimeField(auto_now=True)                                # 글 수정 시간
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    hit_count = models.IntegerField(default=0)    

