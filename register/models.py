# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from datetime import time
# Create your models here.

#tipa zapis k stilistu
def get_default_my_date():
    return "Запись от "+datetime.now().strftime("%d.%m.%Y (%H:%M)")
class Appointment(models.Model):
    title = models.CharField(max_length=255, default=get_default_my_date)
    client_name = models.CharField(max_length=255, verbose_name = "Имя")
    client_patronymic = models.CharField(max_length=255, default="", verbose_name = "Отчество")#otchestvo
    client_phone = models.CharField(max_length=13, verbose_name="Номер телефона")
    appointment_reg_date = models.DateTimeField(auto_now_add=True)
    appointment_beg_date = models.TimeField(verbose_name = "Начало")
    appointment_end_date = models.TimeField(verbose_name = "Конец")
    option = models.ForeignKey('Option',
        on_delete=models.SET_DEFAULT, default=None, verbose_name = "Услуга")#option_id
    stylist = models.ForeignKey('Stylist',
        on_delete=models.SET_DEFAULT, default=None, verbose_name = "Стилист")#stylist_id
    address = models.ForeignKey('Address', on_delete=models.PROTECT, to_field='id', default=1, verbose_name = "Адрес")#address_id
    proof = models.BooleanField(default=False)#podtverzdeno?

    def __str__(self):
        return self.title
#title = models.CharField(max_length=255)#имя файла
class Option(models.Model):
    name = models.CharField(max_length=255, verbose_name = "Наименование")
    price = models.CharField(max_length=255, verbose_name = "Начальная цена")
    #count_time_block = models.IntegerField(default=1,verbose_name = "Кол-во затрачиваемых временных отрезков (по 40 мин.)")
    count_time_block = models.TimeField(default=time(0, 40, 0),verbose_name ="Затрачиваемое время (лучше кратное 40 мин)")

    def __str__(self):
        return self.name
class Stylist(models.Model):
    name = models.CharField(max_length=255, verbose_name = "Имя")
    surname = models.CharField(max_length=255, verbose_name = "Фамилия")
    patronymic = models.CharField(max_length=255, default="", verbose_name = "Отчетсво")
    photo = models.ImageField(upload_to="images/stylists/",default = 'null', null = True)
    about = models.TextField(verbose_name = "О себе")

    def __str__(self):
        return self.name+" "+self.surname
class Address(models.Model):
    city = models.CharField(max_length=255, verbose_name = "Город")
    street = models.CharField(max_length=255, verbose_name ="Улица")
    building = models.CharField(max_length=255,verbose_name = "Здание")

    def __str__(self):
        return self.city+" "+self.street+" "+self.building
# # DAY_CHOICES = (
# #     (datetime.strptime("Mon"), "Понедельник"),
# #     (datetime.strptime("Tue"), "Вторник"),
# #     (datetime.strptime("Wen"), "Среда"),
# #     (datetime.strptime("Thu"), "Четверг"),
# #     (datetime.strptime("Fri"), "Пятница"),
# #     (datetime.strptime("Sat"), "Суббота"),
# #     (datetime.strptime("Sun"), "Воскресенье"),
# # )
# # TIME_CHOICES = (
# #     (time.strptime("9:40", "%H:%M"), "9:40"),
# #     (time.strptime("10:20", "%H:%M"), "10:20"),
# #     (time.strptime("11:00", "%H:%M"), "11:00"),
# #     (time.strptime("11:40", "%H:%M"), "11:40"),
# #     (time.strptime("12:20", "%H:%M"), "12:20"),
# #     (time.strptime("13:00", "%H:%M"), "13:00"),
# #     (time.strptime("13:40", "%H:%M"), "13:40"),
# #     (time.strptime("14:20", "%H:%M"), "14:20"),
# #     (time.strptime("15:00", "%H:%M"), "15:00"),
# #     (time.strptime("15:40", "%H:%M"), "15:40"),
# #     (time.strptime("16:20", "%H:%M"), "16:20"),
# #     (time.strptime("17:00", "%H:%M"), "17:00"),
# #     (time.strptime("17:40", "%H:%M"), "17:40"),
# #     (time.strptime("18:20", "%H:%M"), "18:20"),
# #     (time.strptime("19:00", "%H:%M"), "19:00"),
# #     (time.strptime("19:40", "%H:%M"), "19:40"),
# # )

# class Blocks(models.Model):
#     number = models.IntegerField()#1-16 
#     #time = models.ForeignKey('Times', on_delete=models.PROTECT)#time_id
#     #occupied = models.BooleanField(default=False)#zanato?
#     date = models.DateField()
#     # day_name = DAY_CHOICES
#     # time  = TIME_CHOICES
#     appointment = models.ForeignKey('Appointment', on_delete=models.SET_DEFAULT, default = 'null', null = True)
#     #занятость смотрим по null в appointmemt
#     stylist = models.ForeignKey('Stylist', on_delete=models.PROTECT)
#     address = models.ForeignKey('Address', on_delete=models.PROTECT, default = 0)
    
# # class Times(models.Model):
#     # time_str = models.CharField()
#     # time_clock = models.TimeField()
    
#     # def __str__():
#         # return self.time_str