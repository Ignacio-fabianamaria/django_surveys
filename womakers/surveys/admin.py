# Register your models here.
# https://docs.djangoproject.com/en/5.1/ref/contrib/admin/

from django.contrib import admin
from .models import Question, Option, Vote


class OptionInline(admin.TabularInline):
    model = Option


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ['text', 'options', 'created_at', 'enabled']
    list_filter = ['enabled']
    search_fields = ['text']

    def options(self, obj):
        return obj.option_set.count()


class VoteAdmin(admin.ModelAdmin):
    list_display = ['get_question', 'option', 'created_at']

    def get_question(self, obj):
        # acessa a questão através da opção
        return obj.option.question

    # define a descrição da colunanno admin
    get_question.short_description = 'Question'


admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote, VoteAdmin)
