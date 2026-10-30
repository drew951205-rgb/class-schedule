from django.test import TestCase
from django.urls import reverse
from .models import Course
class ScheduleTests(TestCase):
    def test_create_overlap_edit_and_delete(self):
        data = {'name':'測試課程','teacher':'老師','weekday':1,'start':2,'end':4,'classroom':'教室'}
        self.assertEqual(self.client.post(reverse('add'), data).status_code, 302)
        course = Course.objects.get()
        self.assertEqual(self.client.get(reverse('weekly')).status_code, 200)
        overlap = dict(data, name='衝突課程', start=4, end=5)
        self.assertContains(self.client.post(reverse('add'), overlap), '這段節次已有其他課程')
        adjacent = dict(data, name='下一堂', start=5, end=5)
        self.assertEqual(self.client.post(reverse('add'), adjacent).status_code, 302)
        self.assertEqual(self.client.post(reverse('edit', args=[course.pk]), data).status_code, 302)
        self.assertEqual(self.client.get(reverse('delete', args=[course.pk])).status_code, 200)
        self.assertEqual(self.client.post(reverse('delete', args=[course.pk])).status_code, 302)
