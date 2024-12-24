# Generated by Django 5.1.4 on 2024-12-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='performers/'),
        ),
        migrations.AlterField(
            model_name='performer',
            name='nationality',
            field=models.CharField(blank=True, choices=[('br', 'Brasileiro'), ('us', 'Americano'), ('uk', 'Britânico'), ('fr', 'Francês'), ('it', 'Italiano'), ('jp', 'Japonês'), ('cn', 'Chinês'), ('ru', 'Russo'), ('de', 'Alemão'), ('es', 'Espanhol'), ('ar', 'Argentino'), ('mx', 'Mexicano'), ('co', 'Colombiano'), ('pe', 'Peruano'), ('cl', 'Chileno'), ('ve', 'Venezuelano'), ('ec', 'Equatoriano'), ('bo', 'Boliviano'), ('py', 'Paraguaio'), ('uy', 'Uruguai'), ('other', 'Outro')], max_length=100, null=True),
        ),
    ]