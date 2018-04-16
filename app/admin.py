#encoding:utf-8
from django.contrib import admin
from .models import  Book, BookOrder, Order

# Register your models here.



class BookAdmin(admin.ModelAdmin):
	exclude = ('category',)
	fieldsets = [
		('Info',	{'fields': ['name', 'description', 'price']}),
		('Popularity', {'fields': ['featured', 'popularity']}),
		('Multimedia', {'fields': ['multimedia']}),
	]
	list_display = ('name', 'pub_date', 'price', 'featured', 'popularity')




class BookInline(admin.TabularInline):
	extra = 1
	model = BookOrder
	verbose_name = "Book in this order"
	verbose_name_plural = "Books in order"



class OrderAdmin(admin.ModelAdmin):

	fieldsets = [
		('Order info',	{	'fields': [ 'first_name','total_amount', 'payment',]}),]
	inlines = [ BookInline, ]
	list_display = ('__str__', 'first_name','order_date', 'total_amount', 'user')
	list_filter = ('user', 'order_date',)
	search_fields = ('user__username', 'user__email')




admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)