from django.contrib import admin
from .models import*
from django.utils.safestring import mark_safe

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('images_view','description' ,'titre','create_at', 'update_at' , 'statut', )
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'libelle','titre', 'images_view','create_at','update_at' , 'statut',)
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

@admin.register(Our)
class OurAdmin(admin.ModelAdmin):
    list_display = ('description','titre', 'images_view','create_at','update_at' , 'statut',)
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('description', 'libelle', 'images_view','titre','create_at','update_at' , 'statut',)
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message','telefone','create_at','update_at' , 'statut',)
    