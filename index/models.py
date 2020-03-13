from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name='项目名称')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="开始时间")

    def __str__(self):
        return self.name


class Server(models.Model):
    ip = models.GenericIPAddressField(verbose_name='服务器ip')
    password = models.CharField(max_length=256, verbose_name="服务器密码")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="所属项目")

    def __str__(self):
        return self.project