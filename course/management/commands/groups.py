from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from feud.models import Prompt
from course.models import course

class Command(BaseCommand):
    help = "set up custom groups for application"

    def handle(self, *args, **options):
        instructors = Group(name="instructors")
        instructors.save()
        content_type = ContentType.objects.get_for_model(Prompt)
        permission = Permission.objects.get(content_type=content_type, codename="add_prompt")
        instructors.permissions.add(permission)
        permission = Permission.objects.get(content_type=content_type, codename="change_prompt")
        instructors.permissions.add(permission)
        permission = Permission.objects.get(content_type=content_type, codename="delete_prompt")
        instructors.permissions.add(permission)
        content_type = ContentType.objects.get_for_model(course)
        permission = Permission.objects.get(content_type=content_type, codename="add_course")
        instructors.permissions.add(permission)
        permission = Permission.objects.get(content_type=content_type, codename="change_course")
        instructors.permissions.add(permission)
        permission = Permission.objects.get(content_type=content_type, codename="delete_course")
        instructors.permissions.add(permission)
        instructors.save()
        self.stdout.write(self.style.SUCCESS('Groups created'))
