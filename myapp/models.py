from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from deep_translator import GoogleTranslator  # Using Deep Translator for better translation accuracy

# Define supported languages for FAQ translations
LANGUAGES = {'hi': 'Hindi', 'bn': 'Bengali', 'en': 'English'}

class FAQ(models.Model):
    '''Model to store FAQ with multilingual support using auto-translation.'''

    question = models.TextField()  
    '''Stores the question in the default language (usually English)'''

    answer = RichTextField()  
    '''Stores the answer with WYSIWYG editor support (CKEditor)'''

    question_hi = models.TextField(blank=True, null=True)  
    '''Stores the Hindi translation of the question'''

    answer_hi = RichTextField(blank=True, null=True)  
    '''Stores the Hindi translation of the answer'''

    question_bn = models.TextField(blank=True, null=True)  
    '''Stores the Bengali translation of the question'''

    answer_bn = RichTextField(blank=True, null=True)  
    '''Stores the Bengali translation of the answer'''

    created_at = models.DateTimeField(auto_now_add=True)  
    '''Stores the timestamp when the FAQ was created'''

    def translate_text(self, text, dest_language):
        '''Translates the provided text using GoogleTranslator and caches the result.'''
        cache_key = f"translation_{self.id}_{dest_language}"  # Cache key for storing translations
        cached_translation = cache.get(cache_key)  # Check if translation is cached

        if cached_translation:
            return cached_translation  # Return cached translation if available

        # Translate the text using Deep Translator
        translated_text = GoogleTranslator(
            source='auto',
            target=dest_language
        ).translate(text)

        translated_text = translated_text.encode('utf-8').decode('utf-8')  
        '''Ensure the translated text is correctly encoded and decoded'''

        # Cache the translated text for future use (expires in 1 day)
        cache.set(
            cache_key,
            translated_text,
            timeout=86400  # Cache timeout for 24 hours
        )

        return translated_text

    def get_translated_faq(self, lang):
        '''Returns the translated FAQ (question and answer) based on the language provided.'''
        if lang in LANGUAGES:  # Check if the requested language is supported
            return {
                "question": getattr(self, f'question_{lang}', self.question),  
                '''Fetch the translated question or default to English'''
                "answer": getattr(self, f'answer_{lang}', self.answer),  

               
            }
        return {"question": self.question, "answer": self.answer}  
        '''Default to English if language is not supported'''

    def save(self, *args, **kwargs):
        '''Auto-translates the FAQ content before saving if translations are missing.'''
        if not self.question_hi:  
            self.question_hi = self.translate_text(self.question, 'hi')  # Translate to Hindi
        if not self.answer_hi:  
            self.answer_hi = self.translate_text(self.answer, 'hi')  # Translate to Hindi

        if not self.question_bn:  
            self.question_bn = self.translate_text(self.question, 'bn')  # Translate to Bengali
        if not self.answer_bn:  
            self.answer_bn = self.translate_text(self.answer, 'bn')  # Translate to Bengali

        super().save(*args, **kwargs)  # Save the FAQ entry with all translations

    def __str__(self):
        '''Returns the question as the string representation of the FAQ object'''
        return self.question  # Display the question in the admin panel or elsewhere
