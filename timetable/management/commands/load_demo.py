from django.core.management.base import BaseCommand
from django.db import transaction
from timetable.models import Course


class Command(BaseCommand):
    help = "在空白課表建立示範課程，不會刪除或覆蓋既有資料。"

    @transaction.atomic
    def handle(self, *args, **options):
        if Course.objects.exists():
            self.stdout.write(self.style.WARNING("課表已有資料，未加入示範課程。"))
            return
        rows = [
            ("程式設計", "陳老師", 1, 2, 4, "資訊 401"),
            ("資料庫概論", "林老師", 2, 5, 7, "資訊 402"),
            ("網頁設計", "王老師", 3, 2, 3, "電腦教室"),
            ("管理學", "張老師", 4, 5, 6, "教學 301"),
            ("英文", "李老師", 5, 1, 2, "教學 205"),
        ]
        Course.objects.bulk_create([Course(name=name, teacher=teacher, weekday=day, start=start, end=end, classroom=room) for name, teacher, day, start, end, room in rows])
        self.stdout.write(self.style.SUCCESS("已建立 5 門示範課程。"))
