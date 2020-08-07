from django.db import migrations

def create_data(apps, schema_editor):
    Account = apps.get_model('accounts', 'Account')
    Account(first_name="Customer 001", last_name="Customer 001", email="customer001@email.com", username="pdang" ).save()

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]