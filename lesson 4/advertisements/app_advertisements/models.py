from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Укажите True, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name = "пользователь", on_delete=models.CASCADE,default=1)#пользователь создавший объявление
    image = models.ImageField("изображение", upload_to="advertisements/", null = True, blank = True)

    @admin.display(description = 'дата создания')
    def creation_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description = 'дата обновления')
    def updation_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color: red; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description = 'фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img scr = "{url}" style = "max-width: 80px; max-height:80 px;"', url = self.image.url
            )
        else:
            return format_html(
                '<img scr="{url}" style="max-width: 80px; max-height:80 px"', url='/static/img/adv.png'
            )

    def __str__(self):
        return f"Advertisement(id = {self.id},title = {self.title}, price={self.price})"
    
    class Meta:
        db_table = "advertisements"


