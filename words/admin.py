from django.contrib import admin
from  .models import Word,WordTimeStamp

# Register your models here.
class WordTimeStampModelAdmin(admin.ModelAdmin):
	list_display = ["word","today_count","genral_count"]

	class Meta:
		model = WordTimeStamp



admin.site.register(Word)
admin.site.register(WordTimeStamp,WordTimeStampModelAdmin)