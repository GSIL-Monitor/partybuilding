from django.db import models
from django.db.models import Sum
from django.utils import timezone

from info.models import Member, Branch


class Activity(models.Model):
    name = models.CharField('活动名称', max_length=100)
    date = models.DateTimeField('活动时间', default=timezone.now)
    credit = models.FloatField('学时数', choices=((i / 2, i / 2) for i in range(1, 41)))
    branch = models.ManyToManyField(Branch, verbose_name='主/承方')

    class Meta:
        unique_together = ('name', 'date')
        ordering = ('-date', 'name')
        verbose_name = '党建活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TakePartIn(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='支部成员')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='党建活动')

    def name(self):
        return self.member.name
    name.short_description = '姓名'

    def activity_name(self):
        return self.activity.name
    activity_name.short_description = '活动名称'

    def activity_credit(self):
        return self.activity.credit
    activity_credit.short_description = '活动学时'

    class Meta:
        unique_together = ('activity', 'member')
        ordering = ('activity', 'member')
        verbose_name = '学时统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s: %s" % (self.activity, self.member)
