# Generated by Django 5.0.4 on 2024-06-01 20:42

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_producto_imagen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialcambioproducto',
            name='fecha_cambio',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='historialcambioproducto',
            name='valor_anterior',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='historialcambioproducto',
            name='valor_nuevo',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='ProductoCambio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cambio', models.DateTimeField(default=datetime.datetime.now)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('categorias', models.ManyToManyField(blank=True, to='store.categoria')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.producto')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.proveedor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]