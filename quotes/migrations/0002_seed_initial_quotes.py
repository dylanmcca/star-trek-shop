from django.db import migrations


def seed_quotes(apps, schema_editor):
    Quote = apps.get_model('quotes', 'Quote')

    starter_quotes = [
        (
            'Live long and prosper.',
            'Spock',
            'Star Trek: The Original Series',
        ),
        (
            'Space: the final frontier.',
            'James T. Kirk',
            'Star Trek: The Original Series',
        ),
        (
            'The needs of the many outweigh the needs of the few.',
            'Spock',
            'Star Trek II: The Wrath of Khan',
        ),
        (
            'Make it so.',
            'Jean-Luc Picard',
            'Star Trek: The Next Generation',
        ),
        (
            'Resistance is futile.',
            'The Borg',
            'Star Trek: The Next Generation',
        ),
        (
            'Logic is the beginning of wisdom, not the end.',
            'Spock',
            'Star Trek',
        ),
        (
            'There are four lights!',
            'Jean-Luc Picard',
            'Star Trek: The Next Generation',
        ),
        (
            'Infinite diversity in infinite combinations.',
            'Spock',
            'Star Trek',
        ),
        (
            'Engage.',
            'Jean-Luc Picard',
            'Star Trek: The Next Generation',
        ),
        (
            'I am a doctor, not a bricklayer.',
            'Leonard McCoy',
            'Star Trek: The Original Series',
        ),
    ]

    for quote, character, source in starter_quotes:
        Quote.objects.get_or_create(
            quote=quote,
            character=character,
            source=source,
        )


def unseed_quotes(apps, schema_editor):
    Quote = apps.get_model('quotes', 'Quote')

    quote_texts = [
        'Live long and prosper.',
        'Space: the final frontier.',
        'The needs of the many outweigh the needs of the few.',
        'Make it so.',
        'Resistance is futile.',
        'Logic is the beginning of wisdom, not the end.',
        'There are four lights!',
        'Infinite diversity in infinite combinations.',
        'Engage.',
        'I am a doctor, not a bricklayer.',
    ]

    Quote.objects.filter(quote__in=quote_texts).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_quotes, unseed_quotes),
    ]
