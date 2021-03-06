# Generated by Django 2.1.5 on 2019-02-07 06:41

from django.db import migrations, models
import django.db.models.deletion
import info.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50, unique=True, verbose_name='组织名称')),
                ('date_create', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='成立日期')),
            ],
            options={
                'verbose_name': '基层组织',
                'verbose_name_plural': '基层组织',
                'ordering': ('branch_name',),
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('netid', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='姓名')),
                ('birth_date', models.DateField(max_length=10, verbose_name='出生时间')),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=1, verbose_name='性别')),
                ('group', models.CharField(max_length=20, verbose_name='民族')),
                ('place_birth', models.CharField(max_length=50, verbose_name='籍贯')),
                ('major_in', models.CharField(max_length=30, verbose_name='当前专业（全称）')),
                ('youth_league_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='入团时间')),
                ('constitution_group_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='参加党章学习小组时间')),
                ('application_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='递交入党申请书时间')),
                ('activist_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='确定为入党积极分子时间')),
                ('league_promotion_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='团支部推优时间（重点发展对象）')),
                ('democratic_appraisal_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='民主评议时间')),
                ('political_check_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='政治审查时间')),
                ('key_develop_person_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='确认为重点发展对象时间')),
                ('graduated_party_school_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='党校培训结业时间')),
                ('recommenders_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='确认入党介绍人时间')),
                ('recommenders', models.CharField(blank=True, max_length=50, null=True, verbose_name='入党介绍人')),
                ('autobiography_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='自传')),
                ('application_form_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='入党志愿书')),
                ('first_branch_conference', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='支部大会时间1（支部大会通过成为预备党员）')),
                ('pro_conversation_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='入党谈话时间')),
                ('talker', models.CharField(blank=True, max_length=50, null=True, verbose_name='入党谈话人')),
                ('probationary_approval_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='预备党员时间（党委批准）')),
                ('oach_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='入党宣誓时间')),
                ('application_fullmember_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='转正申请书时间')),
                ('second_branch_conference', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='支部大会时间2（支部大会通过成为正式党员）')),
                ('fullmember_approval_date', info.models.NullableDateField(blank=True, default=None, max_length=10, null=True, verbose_name='正式党员时间（党委批准）')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Branch', verbose_name='支部')),
            ],
            options={
                'verbose_name': '个人信息',
                'verbose_name_plural': '个人信息',
                'ordering': ('branch', 'netid'),
            },
        ),
    ]
