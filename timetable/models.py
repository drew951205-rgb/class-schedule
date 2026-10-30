from django.db import models
class Course(models.Model):
    name = models.CharField('課程名稱', max_length=100)
    teacher = models.CharField('授課老師', max_length=100, blank=True)
    weekday = models.PositiveSmallIntegerField('星期', choices=[(i, '星期' + n) for i,n in enumerate('一二三四五六日', 1)])
    start = models.PositiveSmallIntegerField('開始節次', choices=[(i, f'第 {i} 節') for i in range(1,10)])
    end = models.PositiveSmallIntegerField('結束節次', choices=[(i, f'第 {i} 節') for i in range(1,10)])
    classroom = models.CharField('教室', max_length=100, blank=True)
