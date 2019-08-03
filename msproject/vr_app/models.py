from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"""class HelpData(models.Model):
    question_title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    question_content = models.TextField()
    def __str__(self):
        return self.question_title
    def summary(self):
        return self.body[:100]
"""
# ohjinjin 08/03/19 AM 02:54 커스텀된 유저 모델이 중복되어버려서 문제가 생긴건지 잘 나오질않아여...ㅜㅜ 확인후에 이어서 작업하겠습니다
# https://gyukebox.github.io/blog/django-%EC%84%A4%EC%A0%95-%EB%8D%94%EC%9A%B1-%EC%84%B8%EB%B6%80%EC%A0%81%EC%9C%BC%EB%A1%9C-%EB%B6%84%EB%A6%AC%ED%95%98%EA%B8%B0/
# ohjinjin, 08/03/19 AM 01:39 defined profile class
class Profile2(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  #id,pw,email, firstname, lastname
    evidence = models.ImageField(upload_to = 'images/')
    sex = models.CharField(max_length=15, blank=True)
    birth_date = models.CharField(max_length=15, blank=True)
    phone_number = models.CharField(max_length=15,blank=True)
    agreement1 = models.CharField(max_length=10, blank=True)
    agreement2 = models.CharField(max_length=10, blank=True)