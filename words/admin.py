from django.contrib import admin
from  .models import Word

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["created_at"]

	class Meta:
		model = Word



admin.site.register(Word,PostModelAdmin)