from django.db import models

# Create your models here.

class memberRegister(models.Model):
  user_fstname = models.CharField(max_length=50, verbose_name='이름')
  user_lastmame = models.CharField(max_length=50, verbose_name='성')
  user_email = models.EmailField(max_length=128, verbose_name='이메일')
  user_pwd = models.CharField(max_length=50, verbose_name='비밀번호')

  def __str__(self) -> str:
      return self.user_fstname+"," + self.user_lastmame+"," + self.user_email+"," + self.user_pwd+","