# Generated by Django 2.1.2 on 2018-11-21 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppe3', '0005_auto_20181119_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='adresse',
            name='CLIENT',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppe3.Client'),
        ),
        migrations.AddField(
            model_name='adresse',
            name='livraison',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppe3.livraison'),
        ),
        migrations.AddField(
            model_name='adresse',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppe3.Produit'),
        ),
        migrations.AddField(
            model_name='commande',
            name='Role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppe3.Role'),
        ),
        migrations.AddField(
            model_name='compte',
            name='Role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppe3.Role'),
        ),
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppe3.categorie'),
        ),
    ]
