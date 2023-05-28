from django.test import TestCase
from django.urls import reverse

from posts.models import Post


class PostModeTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEquals(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_view_url_exists(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)
