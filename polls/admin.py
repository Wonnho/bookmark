from django.contrib import admin

from .models import Question, Choice


# Register your models here.


    
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets= [
        ('질문',  {'fields':['question_text']}), 
        ('날짜', {'fields':['pub_date']}),
        
      
    ]
    
    list_display=('question_text','pub_date','was_published_recently')
    inlines=[ChoiceInline]

    list_filter=['pub_date']
    search_fields=['question_text']



admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
