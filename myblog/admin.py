from django.contrib import admin
from myblog.models import Post, Category


#@admin.register(Post, Category)
#class Post(admin.ModelAdmin):
#    pass
##    fieldsets = ((None, {
##            'fields': ('title', 'text', 'author', 'published_date')
##            }),
##            ('Advanced options', {
##                    'classes': ('collapse',),
##                    'fields': ('name', 'description', 'posts'),
##            }),
##    )



class PostCatInline(admin.TabularInline):
    model = Category.posts.through
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'published_date')
    inlines = [PostCatInline,]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines =[PostCatInline,]
    exclude = ('posts',)
    

#admin.site.register(Post)
#admin.site.register(Category)

#admin.site.register(Post)
#
#class PostInline(admin.TabularInline):
#    model = Category.posts.through
#    
#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin):
#    inlines = (PostInline,)
#    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
#admin.site.register(PairPostCategory)