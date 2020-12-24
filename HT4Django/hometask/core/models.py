from django.db import models


class Guilds(models.Model):
    title = models.CharField(max_length=255, null=True, default="some guild", verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Гильдия"
        verbose_name_plural = "Гильдии"


class Player(models.Model):
    sex = ([1, 'Male'], [2, 'Female'])
    fractions = ([1, 'Alliance'], [2, 'Horde'])
    races = (
        [1, 'Human'],
        [2, 'Dwarf'],
        [3, 'Night Elf'],
        [4, 'Gnome'],
        [5, 'Draenei'],
        [6, 'Worgen'],
        [7, 'Pandaren'],
        [8, 'Orc'],
        [9, 'Undead'],
        [10, 'Tauren'],
        [11, 'Troll'],
        [12, 'Blood Elf'],
        [13, 'Goblin']
    )
    classes = (
        [1, 'Warrior'],
        [2, 'Paladin'],
        [3, 'Hunter'],
        [4, 'Rogue'],
        [5, 'Priest'],
        [6, 'Shaman'],
        [7, 'Mage'],
        [8, 'Warlock'],
        [9, 'Monk'],
        [10, 'Druid'],
        [11, 'Demon Hunter'],
        [12, 'Death Knight'],
    )
    nickname = models.CharField(max_length=255, null=False, default="Player", verbose_name="Ник")
    fraction = models.IntegerField(choices=fractions, null=False, default=1, verbose_name="Фракция")
    race = models.IntegerField(choices=races, null=False, default=1, verbose_name="Расса")
    sex = models.IntegerField(choices=sex, null=False, default=1, verbose_name="Пол")
    klass = models.IntegerField(choices=classes, null=False, default=1, verbose_name="Класс")
    level = models.IntegerField(null=False, default=1, verbose_name="Уровень")
    guild = models.ForeignKey(Guilds, null=True, default="Without Guild", on_delete=models.SET("Without guild"),
                              verbose_name="Гильдия")

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"
