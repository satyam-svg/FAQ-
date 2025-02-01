from django.db import migrations

def create_initial_faqs(apps, schema_editor):
    """Create initial FAQ entries with auto-generated translations."""
    FAQ = apps.get_model('myapp', 'FAQ')  # Correct model reference

    faq_data = [
        {
            "question": "What is Django?",
            "answer": "Django is a Python-based web framework."
        },
        {
            "question": "What is Python?",
            "answer": "Python is a programming language."
        },
        {
            "question": "How to install Django?",
            "answer": "You can install Django using pip: pip install django"
        },
    ]

    for faq_entry in faq_data:
        ''' Create FAQ instance'''
        faq = FAQ(
            question=faq_entry["question"],
            answer=faq_entry["answer"]
        )

        '''Generate translations using the model's translate_text method'''
        faq.question_hi = faq.translate_text(faq_entry["question"], 'hi')
        faq.answer_hi = faq.translate_text(faq_entry["answer"], 'hi')  # Fixed this line
        faq.question_bn = faq.translate_text(faq_entry["question"], 'bn')
        faq.answer_bn = faq.translate_text(faq_entry["answer"], 'bn')  # Fixed this line

        '''Save the FAQ entry'''
        faq.save()

def remove_initial_faqs(apps, schema_editor):
    """Remove initial FAQ entries."""
    FAQ = apps.get_model('myapp', 'FAQ')
    FAQ.objects.filter(question__in=["What is Django?", "What is Python?", "How to install Django?"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_faq_answer_bn_faq_answer_hi'),  # Replace with the correct previous migration number
    ]

    operations = [
        migrations.RunPython(create_initial_faqs, remove_initial_faqs),
    ]
