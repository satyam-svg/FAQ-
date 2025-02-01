from django.http import JsonResponse
from .models import FAQ

def get_faqs(request):
    lang = request.GET.get('lang', None)  # URL se lang parameter fetch karein
    valid_langs = ['en', 'hi', 'bn']  # Supported languages

    faqs = FAQ.objects.all()

    if lang and lang in valid_langs:
        # Sirf requested language return karein
        data = [
            {
                "question": getattr(faq, f'question_{lang}', faq.question),
                "answer": getattr(faq, f'answer_{lang}', faq.answer)
            }
            for faq in faqs
        ]
    else:
        '''If theres is no query then return all the data'''
        data = [
            {
                "question_en": faq.question,
                "answer_en": faq.answer,
                "question_hi": faq.question_hi,
                "answer_hi": faq.answer_hi,
                "question_bn": faq.question_bn,
                "answer_bn": faq.answer_bn,
            }
            for faq in faqs
        ]

    return JsonResponse({"faqs": data}, safe=False, json_dumps_params={'ensure_ascii': False})
