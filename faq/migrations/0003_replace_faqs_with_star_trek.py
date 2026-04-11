from django.db import migrations


def replace_with_star_trek_faqs(apps, schema_editor):
    FAQ = apps.get_model('faq', 'FAQ')
    
    # Clear all existing FAQs
    FAQ.objects.all().delete()
    
    # Add playful Star Trek Q&As
    star_trek_faqs = [
        (
            'How long until my order reaches my quadrant?',
            'Most orders are processed within 1-2 Earth business days. UK deliveries usually arrive in 2-4 days after dispatch, while interstellar (international) deliveries typically take 7-14 days.',
        ),
        (
            'Do you deliver beyond Federation space?',
            'Yes. We ship worldwide. Final shipping costs and travel time are calculated at checkout based on your planetary coordinates.',
        ),
        (
            'Will I receive tracking for my shipment?',
            'Absolutely. Once your order leaves spacedock, we\'ll send a dispatch email with a tracking link so you can monitor its journey.',
        ),
        (
            'What is your return policy, Captain?',
            'You can return most unused items within 30 days of delivery for a refund or exchange. Returned items must be in original condition and packaging.',
        ),
        (
            'My order arrived damaged by an ion storm. What now?',
            'Contact us within 7 days of delivery with your order number and photos of the issue. We\'ll arrange a replacement or refund at warp speed.',
        ),
        (
            'Can I exchange for a different size uniform?',
            'Yes, if your preferred size is in stock. Message us and we\'ll guide you through the exchange process.',
        ),
        (
            'Are your products officially licensed by Starfleet Command?',
            'Licensing varies by product. Officially licensed items are clearly marked in each product description.',
        ),
        (
            'Can I cancel or change my order after I place it?',
            'If your order hasn\'t been dispatched yet, we can usually make changes or cancel it. Contact us quickly and we\'ll do our best.',
        ),
        (
            'Do you offer gifts for fellow crew members?',
            'Yes, gift options are available on selected items. Where available, you can add gift wrapping and a custom message at checkout.',
        ),
        (
            'What payment methods do you accept on the bridge?',
            'We accept major credit/debit cards and secure payment options shown at checkout. All payments are encrypted for your security.',
        ),
    ]
    
    for question, answer in star_trek_faqs:
        FAQ.objects.create(question=question, answer=answer)


def reverse_to_plain_faqs(apps, schema_editor):
    FAQ = apps.get_model('faq', 'FAQ')
    FAQ.objects.all().delete()
    
    # Restore original plain FAQs if rolling back
    plain_faqs = [
        ('How long does shipping take?', 'Orders are processed in 1-2 business days. UK delivery is usually 2-4 business days after dispatch, and international delivery is typically 7-14 business days.'),
        ('Do you ship internationally?', 'Yes, we ship worldwide. Shipping rates and delivery times are calculated at checkout based on destination.'),
        ('Can I track my order?', 'Yes. Once your order is dispatched, we email a tracking link so you can follow your parcel.'),
        ('What is your return policy?', 'Most unused items can be returned within 30 days of delivery for a refund or exchange, provided they are in original condition and packaging.'),
        ('What if my item arrives damaged or incorrect?', 'Contact us within 7 days of delivery with your order number and photos. We will arrange a replacement or refund quickly.'),
        ('Can I exchange for a different size?', 'Yes, if the requested size is in stock. Contact us and we will guide you through the exchange process.'),
        ('Are your products officially licensed?', 'Licensing varies by product. Officially licensed items are clearly marked in each product description.'),
        ('Can I cancel or change my order after placing it?', 'If your order has not shipped yet, we can usually help. Contact us as soon as possible after placing your order.'),
        ('Do you offer gift wrapping or gift messages?', 'Gift options are available on selected items and can be chosen at checkout where available.'),
        ('Which payment methods do you accept?', 'We accept major credit and debit cards plus secure online payment methods shown at checkout.'),
    ]
    
    for question, answer in plain_faqs:
        FAQ.objects.create(question=question, answer=answer)


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_seed_initial_faqs'),
    ]

    operations = [
        migrations.RunPython(replace_with_star_trek_faqs, reverse_to_plain_faqs),
    ]
