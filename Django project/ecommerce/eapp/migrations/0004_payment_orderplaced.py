# Generated by Django 4.2.7 on 2023-12-11 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eapp', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Tangail', 'Tangail'), ('Gazipur', 'Gazipur'), ('Faridpur', 'Faridpur'), ('Gopalganj', 'Gopalganj'), ('Jamalpur', 'Jamalpur'), ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Netrokona', 'Netrokona'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Bogra', 'Bogra'), ('Joypurhat', 'Joypurhat'), ('Naogaon', 'Naogaon'), ('Natore', 'Natore'), ('Nawabganj', 'Nawabganj'), ('Pabna', 'Pabna'), ('Rajshahi', 'Rajshahi'), ('Sirajgonj', 'Sirajgonj'), ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'), ('Nilphamari', 'Nilphamari'), ('Panchagarh', 'Panchagarh'), ('Rangpur', 'Rangpur'), ('Thakurgaon', 'Thakurgaon'), ('Barguna', 'Barguna'), ('Barisal', 'Barisal'), ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Bandarban', 'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chittagong', 'Chittagong'), ('Comilla', 'Comilla'), ('Coxs Bazar', 'Coxs Bazar'), ('Feni', 'Feni'), ('Khagrachari', 'Khagrachari'), ('Lakshmipur', 'Lakshmipur'), ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati'), ('Habiganj', 'Habiganj'), ('Maulvibazar', 'Maulvibazar'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Chuadanga'), ('Jessore', 'Jessore'), ('Jhenaidah', 'Jhenaidah'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'), ('Satkhira', 'Satkhira')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.customer')),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eapp.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
