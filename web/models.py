from django.db import models


#Модель группы
class Group(models.Model):
    faculty = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    course = models.IntegerField()
    number = models.CharField(max_length=50)


#Модель преподаватели
class Teacher(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)


#Модель предметы
class Subject(models.Model):
    title_subject = models.CharField(max_length=50)


#Модель номер пары
class Pair_Number(models.Model):
    start_pair = models.TimeField()
    end_pair = models.TimeField()


#Модель аудитории
class Auditorium(models.Model):
    building = models.IntegerField()
    floor = models.IntegerField()
    number_auditorium = models.IntegerField()


#Модель расписание
class Schedule(models.Model):
    date = models.DateField()
    number_pair = models.ForeignKey(Pair_Number, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)

