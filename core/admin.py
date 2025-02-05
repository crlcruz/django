from django.contrib import admin
from core.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'qtde', 'slug', 'dtcriacao', 'dtalteracao', 'ativo', 'imagem')
