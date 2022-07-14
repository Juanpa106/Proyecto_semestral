# Generated by Django 3.1 on 2022-07-14 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito_Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.IntegerField()),
                ('marca_producto', models.CharField(max_length=50)),
                ('imagen_producto', models.ImageField(null=True, upload_to='carrito_compras')),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'db_Carrito',
            },
        ),
        migrations.CreateModel(
            name='Subscripcion',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('suscrito', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'db_Subscripcion',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'db_Tipo_usuario',
            },
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('run', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=12)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipousuario')),
            ],
            options={
                'db_table': 'db_Usuario',
            },
        ),
        migrations.CreateModel(
            name='Producto_Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('marca', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrito_compras')),
            ],
            options={
                'db_table': 'Historial',
            },
        ),
    ]