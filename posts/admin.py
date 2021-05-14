from django.contrib import admin
from .models import Post, Comment, Category


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


# class CategoryInline(admin.TabularInline):
#     model = Category.post.through
#     extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'body', 'created_at')
    list_display_links = ('title',)
    # inlines = [CommentInline, CategoryInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment', 'rating', 'created_at')
    list_display_links = ('comment',)


# class PostInlineAdmin(admin.TabularInline):
#     model = Category.post.through
#     extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_display_links = ('name',)
    # inlines = [PostInlineAdmin]
