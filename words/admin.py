from django.contrib import admin
from  .models import UserWord, WordTimeStamp, GeneralWord

# Register your models here.
class WordTimeStampModelAdmin(admin.ModelAdmin):
	list_display = ["word"]
	list_filter =  ["word"]

	class Meta:
		model = WordTimeStamp


# # Register your models here.
# class WordModelAdmin(admin.ModelAdmin):
# 	# TODO
# 	# list_display = ["name", "created_at"]
#
# 	class Meta:
# 		model = UserWord

admin.site.register(UserWord)
admin.site.register(WordTimeStamp,WordTimeStampModelAdmin)
admin.site.register(GeneralWord)
