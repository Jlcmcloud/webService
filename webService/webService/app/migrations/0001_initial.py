# Generated by Django 5.0.6 on 2024-06-14 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'db_categoria',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(choices=[(1, 'Aceptado'), (2, 'En proceso'), (3, 'Enviado'), (4, 'Finalizado'), (5, 'Reembolsado'), (6, 'Pendiente de pago')], primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('marca', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'db_cliente',
            },
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
            options={
                'db_table': 'db_carrito',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('subtotal', models.IntegerField(null=True)),
                ('iva', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estado')),
            ],
            options={
                'db_table': 'pedido',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateField()),
                ('estado_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estadopago')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.metodopago')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(default=0)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrito')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'db_table': 'db_item_carrito',
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id_transaccion', models.IntegerField(primary_key=True, serialize=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pago')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'unique_together': {('pedido', 'producto')},
            },
        ),
    ]
