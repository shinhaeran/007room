from django.db import models
from django.utils import timezone
from django.db import models
from multiselectfield import MultiSelectField
#from array_field_select.fields import ArrayField

def default_city(): # user가 회원가입할 때 지정한? 도시 or seoul
    return "seoul"

class User(models.Model):
    email = models.EmailField()                       
    nickname = models.CharField(max_length=10)        
    area = models.CharField(max_length=10)
    report_count = models.IntegerField(default=0)             #신고횟수
    podo = models.IntegerField(default=10)             # 초기10알
    gender = models.BooleanField(default=False)    
    profile_image = models.FileField(null=True, blank=True)
    #keywords = models.CharField()                      #보류


class Post(models.Model):
    Location_list =(
        ('서울특별시','서울특별시'),
        ('부산광역시','부산광역시'),
        ('세종특별시','세종특별시'),
        ('충청북도','충청북도'),
        ('충청남도','충청남도'),
        ('전라북도','전라북도'),
        ('전라남도','전라남도'),
        ('대구광역시','대구광역시'),
        ('제주특별시','제주특별시'),
        ('경상북도','경상북도'),
        ('경상남도','경상남도'),     
    )

    Category_list = (  
        ('study','StudyRoom'), 
        ('performance','PerformanceRoom'),
        ('practice','PracticeRoom'),
        ('etc','etc'),
    )
    
    Option_list =(
        ('vim','vim'),
        ('board', 'board'),
        ('desk', 'desk'),
        ('multitap','multitap'),
        ('speaker','speaker'),
        ('lights','lights'),
        ('mirror','mirror'),
        ('air','airconditioner'),
        ('printer','printer'),
    )

        
    title = models.CharField(max_length=50)
    context = models.TextField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    choose_date = models.DurationField() #!!!!!!! 일정 기간을 저장하는 필드를 만들기    
    '''지역 선택'''
    #location = ArrayField( models.CharField(choices=Location_list, max_length=30, default=default_city))
    '''공간 유형 선택'''
    category = MultiSelectField(choices=Category_list, max_length=50, blank=True)
    etc_what = models.CharField(max_length=50, null=True,blank=True)
    '''물건 대여 선택'''
    Option = MultiSelectField(choices=Option_list, max_length=50,default=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)  # 글 작성 시간 :  시간이 있는 날짜를 저장하는 datetime 필드를 만들기 
    Modified_date = models.DateTimeField(auto_now=True) # 글 게시 날짜 

    def __str__(self):
        return "RoomShare : {}".format(self.title)
    
    def ROOM_TYPE(self):
        if self.category=='etc' :
            return "ROOM etc :{}".format(self.etc_what) 

class Review(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(null=True)


class Qna(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirm = models.BooleanField(default=False)
    context = models.TextField()


class Image(models.Model):
    images = models.ImageField() 
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


class Qna_image(Image):
    qna = models.ForeignKey(Qna, default=None, on_delete=models.CASCADE)


class Post_image(Image):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)


class Date(models.Model):
    day = models.IntegerField(default=1)
    start_time = models.IntegerField(default=0)
    end_time = models.IntegerField(default=0)


class Like(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


class Post_like(Like):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)


class Review_like(Like):
    review = models.ForeignKey(Review, default=None, on_delete=models.CASCADE)



