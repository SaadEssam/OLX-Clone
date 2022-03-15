# Generated by Django 4.0.3 on 2022-03-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(choices=[('Alexandria', 'Alexandria'), ('Aswan', 'Aswan'), ('Asyut', 'Asyut'), ('Beheira', 'Beheira'), ('Beni Suef', 'Beni Suef'), ('Cairo', 'Cairo'), ('Dakahlia', 'Dakahlia'), ('Damietta', 'Damietta'), ('Fayoum', 'Fayoum'), ('Gharbia', 'Gharbia'), ('Giaz', 'Giza'), ('Ismailia', 'Ismailia'), ('Kafr al-Sheikh', 'Kafr al-Sheikh'), ('Luxor', 'Luxor'), ('Matruh', 'Matruh'), ('Minya', 'Minya'), ('Monufia', 'Monufia'), ('New Valley', 'New Valley'), ('Port Said', 'Port Said'), ('Qalyubia', 'Qalyubia'), ('Qena', 'Qena'), ('Red Sea', 'Red Sea'), ('Sharqia', 'Sharqia'), ('Sohag', 'Sohag'), ('South Sinai', 'South Sinai'), ('Suez', 'Suez')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
