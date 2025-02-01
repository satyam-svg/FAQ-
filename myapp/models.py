from django.db import models
<<<<<<< HEAD
from ckeditor.fields import RichTextField
from django.core.cache import cache
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup  # For handling HTML content in answers

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
        if not text:  # If text is empty, return an empty string
            return ""

        cache_key = f"translation_{hash(text)}_{dest_language}"  # Cache key based on text content
        cached_translation = cache.get(cache_key)  # Check if translation is cached

        if cached_translation:
            return cached_translation  # Return cached translation if available

        try:
            translated_text = GoogleTranslator(source='auto', target=dest_language).translate(text)
            translated_text = translated_text.encode('utf-8').decode('utf-8')  # Ensure correct encoding
        except Exception as e:
            translated_text = text  # Fallback to original text if translation fails
            print(f"Translation error: {e}")  # Debugging info

        # Cache the translated text for future use (expires in 1 day)
        cache.set(cache_key, translated_text, timeout=86400)

        return translated_text

    def clean_html(self, html_text):
        '''Extracts plain text from HTML content to ensure accurate translation.'''
        soup = BeautifulSoup(html_text, "html.parser")
        return soup.get_text()  # Extract only text content from HTML

    def get_translated_faq(self, lang):
        '''Returns the translated FAQ (question and answer) based on the language provided.'''
        if lang in LANGUAGES:  # Check if the requested language is supported
            return {
                "question": getattr(self, f'question_{lang}', self.question),  
                "answer": getattr(self, f'answer_{lang}', self.answer),  
            }
        return {"question": self.question, "answer": self.answer}  

    def save(self, *args, **kwargs):
        '''Auto-translates the FAQ content before saving if translations are missing.'''

        # Translate question fields
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')

        # Translate answer fields (after stripping HTML)
        if not self.answer_hi:
            plain_answer = self.clean_html(self.answer)  # Remove HTML for translation
            translated_answer_hi = self.translate_text(plain_answer, 'hi')
            self.answer_hi = f"<p>{translated_answer_hi}</p>"  # Re-wrap in basic HTML

        if not self.answer_bn:
            plain_answer = self.clean_html(self.answer)  # Remove HTML for translation
            translated_answer_bn = self.translate_text(plain_answer, 'bn')
            self.answer_bn = f"<p>{translated_answer_bn}</p>"  # Re-wrap in basic HTML

        super().save(*args, **kwargs)  # Save the FAQ entry with translations

    def __str__(self):
        '''Returns the question as the string representation of the FAQ object'''
        return self.question  # Display the question in the admin panel or elsewhere
=======

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    published_date=models.DateField(auto_now_add=True)

    def _str_(self):
        return self.title
>>>>>>> 1e92602 (Create a Django FAQ backend app)
