from django.contrib import admin
from .models import Grupo, Aluno

admin.site.register(Grupo)
admin.site.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<account_id>.+)/deposit/$',
                self.admin_site.admin_view(self.process_deposit),
                name='account-deposit',
            )
        ]
        return custom_urls + urls

