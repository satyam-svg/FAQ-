# myapp/migrations/000X_add_initial_faqs.py
from django.db import migrations

def create_initial_faqs(apps, schema_editor):
    FAQ = apps.get_model('myapp', 'FAQ')

    # Add FAQ entries with translations
    FAQ.objects.get_or_create(
        question="What is Django?",
        answer="Django is a Python-based web framework.",
        question_hi="Django क्या है?",
        answer_hi="Django एक Python-आधारित वेब फ्रेमवर्क है।",
        question_bn="Django কী?",
        answer_bn="Django একটি পাইথন ভিত্তিক ওয়েব ফ্রেমওয়ার্ক।"
    )
    FAQ.objects.get_or_create(
        question="What is Python?",
        answer="Python is a programming language.",
        question_hi="Python क्या है?",
        answer_hi="Python एक प्रोग्रामिंग भाषा है।",
        question_bn="Python কী?",
        answer_bn="Python একটি প্রোগ্রামিং ভাষা।"
    )
    FAQ.objects.get_or_create(
        question="How to install Django?",
        answer="You can install Django using pip: pip install django",
        question_hi="Django कैसे इंस्टॉल करें?",
        answer_hi="आप pip का उपयोग करके Django इंस्टॉल कर सकते हैं: pip install django",
        question_bn="Django কীভাবে ইনস্টল করবেন?",
        answer_bn="আপনি pip ব্যবহার করে Django ইনস্টল করতে পারেন: pip install django"
    )

def remove_initial_faqs(apps, schema_editor):
    FAQ = apps.get_model('myapp', 'FAQ')
    FAQ.objects.filter(question__in=["What is Django?", "What is Python?", "How to install Django?"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_faq_answer_bn_faq_answer_hi'),  # Replace with previous migration
    ]

    operations = [
        migrations.RunPython(create_initial_faqs, remove_initial_faqs),
    ]
