# Generated by Django 5.1.3 on 2024-11-26 20:11

import board.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_candidateimage_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='candidate',
            options={'ordering': ['user__first_name', 'user__last_name']},
        ),
        migrations.AlterModelOptions(
            name='candidateimage',
            options={'ordering': ['-is_primary', '-created_at']},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'ordering': ['-completed_at']},
        ),
        migrations.AddField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='candidateimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='candidateimage',
            name='is_primary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidateimage',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='total_questions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='certificate_path',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='result',
            name='completed_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='result',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default='no-reply@example.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='candidateimage',
            name='image',
            field=models.ImageField(upload_to='store/images/%Y/%m', validators=[board.validators.vaidate_file_size]),
        ),
        migrations.AlterField(
            model_name='exam',
            name='duration',
            field=models.DurationField(help_text='Duration in minutes'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='pass_mark',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_results', to='board.candidate'),
        ),
        migrations.AlterField(
            model_name='result',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='board.exam'),
        ),
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('candidate', 'exam')},
        ),
        migrations.AddIndex(
            model_name='candidate',
            index=models.Index(fields=['email'], name='board_candi_email_deeb77_idx'),
        ),
        migrations.AddIndex(
            model_name='exam',
            index=models.Index(fields=['is_active', '-created_at'], name='board_exam_is_acti_4fb2f2_idx'),
        ),
        migrations.AddIndex(
            model_name='result',
            index=models.Index(fields=['candidate', 'exam'], name='board_resul_candida_d7c286_idx'),
        ),
        migrations.AddIndex(
            model_name='result',
            index=models.Index(fields=['is_passed', '-completed_at'], name='board_resul_is_pass_d01f4a_idx'),
        ),
    ]
