from django.contrib import admin
<<<<<<< HEAD
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    '''Custom admin view for FAQ model'''
    
    # Fields to display in the list view
    list_display = ('question', 'created_at', 'question_hi', 'question_bn')
    
    # Search bar for question and translations
    search_fields = ('question', 'question_hi', 'question_bn')
    
    # Fields to display in the form view
    fields = ('question', 'answer', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn')
    
    # Filtering options for the admin list view
    list_filter = ('created_at',)

# Register the FAQ model with custom admin view
admin.site.register(FAQ, FAQAdmin)
=======
from .models import Book
# Register your models here.
admin.site.register(Book)

>>>>>>> 1e92602 (Create a Django FAQ backend app)
