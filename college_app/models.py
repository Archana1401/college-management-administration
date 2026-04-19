from django.db import models

# Create your models here.
class Department(models.Model):
    d_id=models.IntegerField(unique=True)
    dep=[('civil','CIVIL'),('csc','CSC'),('ece','ECE'),('mech','MECH')]
    d_name=models.CharField(max_length=50,choices=dep)

    def __str__(self):
        return self.d_name


class Teachers(models.Model):
    f_id=models.IntegerField(unique=True)
    f_name=models.CharField(max_length=40)
    f_dep=models.ForeignKey(Department,on_delete=models.CASCADE)


    
    def __str__(self):
        return self.f_name


class Students(models.Model):
    s_id=models.IntegerField(unique=True)
    s_name = models.CharField(max_length=100)
    s_dep = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name

    