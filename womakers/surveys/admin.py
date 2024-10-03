from django.contrib import admin
from surveys.models import Question, Option

# Register your models here.
# https://docs.djangoproject.com/en/5.1/ref/contrib/admin/

class OptionInLine(admin.TabularInline):
    model = Option


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInLine]
    list_display = ['text', 'options', 'created_at', 'enabled']
    list_filter = ['enabled']
    search_fields = ['text']

    def options(self, obj):
        return obj.option_set.count()


admin.site.register(Question, QuestionAdmin)
