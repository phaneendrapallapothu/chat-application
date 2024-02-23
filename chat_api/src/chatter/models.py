from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy


class Room(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rooms",
        verbose_name=gettext_lazy("User"),
    )
    name = models.CharField(max_length=255, verbose_name=gettext_lazy("Room Name"))
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=gettext_lazy("Created")
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=gettext_lazy("Updated"))

    class Meta:
        verbose_name = gettext_lazy("Room")
        verbose_name_plural = gettext_lazy("Rooms")
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"], name="unique_user_room_name"
            )
        ]

    def __str__(self):
        return self.name
