import django.db.models.deletion
from django.db import migrations, models

def set_default_shop(apps, schema_editor):
    BankAccount = apps.get_model('store', 'BankAccount')
    Shop = apps.get_model('store', 'Shop')
    default_shop = Shop.objects.first()  # or create a new shop if none exists

    if not default_shop:
        default_shop = Shop.objects.create(name="Default Shop", account=1)  # Ensure you set a valid account ID

    for bankaccount in BankAccount.objects.all():
        bankaccount.shop = default_shop
        bankaccount.save()

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0052_bankaccount_account_alter_bankaccount_accountnumber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='account',
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='shop',
            field=models.ForeignKey(default=None, null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.shop'),
        ),
        migrations.RunPython(set_default_shop),
        migrations.AlterField(
            model_name='bankaccount',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shop'),
        ),
    ]
