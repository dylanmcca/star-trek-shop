from django.db import migrations


def seed_faqs(apps, schema_editor):
    FAQ = apps.get_model('faq', 'FAQ')

    starter_faqs = [
        (
            'How long does shipping take?',
            'Orders are processed in 1-2 business days. UK delivery is usually 2-4 business days after dispatch, and international delivery is typically 7-14 business days.',
        ),
        (
            'Do you ship internationally?',
            'Yes, we ship worldwide. Shipping rates and delivery times are calculated at checkout based on destination.',
        ),
        (
            'Can I track my order?',
            'Yes. Once your order is dispatched, we email a tracking link so you can follow your parcel.',
        ),
        (
            'What is your return policy?',
            'Most unused items can be returned within 30 days of delivery for a refund or exchange, provided they are in original condition and packaging.',
        ),
        (
            'What if my item arrives damaged or incorrect?',
            'Contact us within 7 days of delivery with your order number and photos. We will arrange a replacement or refund quickly.',
        ),
        (
            'Can I exchange for a different size?',
            'Yes, if the requested size is in stock. Contact us and we will guide you through the exchange process.',
        ),
        (
            'Are your products officially licensed?',
            'Licensing varies by product. Officially licensed items are clearly marked in each product description.',
        ),
        (
            'Can I cancel or change my order after placing it?',
            'If your order has not shipped yet, we can usually help. Contact us as soon as possible after placing your order.',
        ),
        (
            'Do you offer gift wrapping or gift messages?',
            'Gift options are available on selected items and can be chosen at checkout where available.',
        ),
        (
            'Which payment methods do you accept?',
            'We accept major credit and debit cards plus secure online payment methods shown at checkout.',
        ),
    ]

    for question, answer in starter_faqs:
        FAQ.objects.get_or_create(question=question, defaults={'answer': answer})


def unseed_faqs(apps, schema_editor):
    FAQ = apps.get_model('faq', 'FAQ')
    questions = [
        'How long does shipping take?',
        'Do you ship internationally?',
        'Can I track my order?',
        'What is your return policy?',
        'What if my item arrives damaged or incorrect?',
        'Can I exchange for a different size?',
        'Are your products officially licensed?',
        'Can I cancel or change my order after placing it?',
        'Do you offer gift wrapping or gift messages?',
        'Which payment methods do you accept?',
    ]
    FAQ.objects.filter(question__in=questions).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_faqs, unseed_faqs),
    ]
