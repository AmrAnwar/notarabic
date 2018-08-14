from django.contrib import admin
from  .models import Word, WordTimeStamp

# Register your models here.
class WordTimeStampModelAdmin(admin.ModelAdmin):
    list_display = ["word", "today_count", "genral_count", "created_at"]
    list_editable = [ "created_at"]

    class Meta:
        model = WordTimeStamp

class WordModel(admin.ModelAdmin):
    list_display = ["name", "created_at"]

    class Meta:
        model = Word



admin.site.register(Word, WordModel)
admin.site.register(WordTimeStamp, WordTimeStampModelAdmin)
