from django.contrib import admin
from .models import Question, Choice, Vote, UserProfile


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'expiration_date', 'is_active')
    list_filter = ['pub_date', 'expiration_date']
    search_fields = ['question_text']
    inlines = [ChoiceInLine]


class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'choice', 'voted_at')
    list_filter = ['question', 'voted_at']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(UserProfile, UserProfileAdmin)