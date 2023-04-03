# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

#tipa zapis k stilistu
# class Appointment(models.Model):
#     client_name = models.CharField(max_length=255, verbose_name = "Имя")
#     client_patronymic = models.CharField(max_length=255, verbose_name = "Отчество")#otchestvo
#     client_phone = models.CharField(max_length=13, verbose_name="Номер телефона")
#     appointment_reg_date = models.DateTimeField(auto_now_add=True)
#     appointment_beg_date = models.DateTimeField(verbose_name = "Начало")
#     appointment_end_date = models.DateTimeField(verbose_name = "Конец")
#     option = models.ForeignKey('Option', 
#         on_delete=models.SET_DEFAULT,default=None, verbose_name = "Услуга")#option_id
#     stylist = models.ForeignKey('Stylist', 
#         on_delete=models.PROTECT, verbose_name = "Стилист")#stylist_id
#     address = models.ForeignKey('Address', on_delete=models.PROTECT, verbose_name = "Адрес")#address_id
#     proof = models.BooleanField(default=False)#podtverzdeno?
    
    
#     def get_absolute_url(self):
#         #Returns the url to access a particular instance.
#         return reverse('appointmemt', args=[str(self.id)])


# class Option(models.Model):
#     name = models.CharField(max_length=255, verbose_name = "Наименование")
#     price = models.CharField(max_length=255, verbose_name = "Начальная цена")
#     count_time_block = models.IntegerField(verbose_name = "Кол-во затрачиваемых временных отрезков (по 40 мин.)")

#     def __str__(self):
#         return self.name

# class Stylist(models.Model):
#     name = models.CharField(max_length=255, verbose_name = "Имя")
#     surname = models.CharField(max_length=255, verbose_name = "Фамилия")
#     patronymic = models.CharField(max_length=255, verbose_name = "Отчетсво")
#     def __str__(self):
#         return self.surname + ' ' + self.name

# class Address(models.Model):
#     city = models.CharField(max_length=255, verbose_name = "Город")
#     street = models.CharField(max_length=255, verbose_name ="Улица")
#     building = models.CharField(max_length=255,verbose_name = "Здание")
    
#     def __str__(self):
#         full_address =''
#         full_address += self.street + ' '
#         full_address += self.building + ' '
#         return full_address

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