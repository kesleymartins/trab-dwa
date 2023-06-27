# Generated by Django 4.2.2 on 2023-06-27 21:50

import aluno.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_rename_frade_student_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='situation',
            field=models.CharField(choices=[(aluno.enums.Situation['CURSANDO'], 'Cursando'), (aluno.enums.Situation['APROVADO'], 'Aprovado'), (aluno.enums.Situation['REPROVADO'], 'Reprovado')], default=aluno.enums.Situation['APROVADO'], max_length=100),
        ),
    ]