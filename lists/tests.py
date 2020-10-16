from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from lists.models import Item

# Create your tests here.
from django.urls import resolve

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # 检查网站根路径‘/'，能否找到名为home_page的函数
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text' : 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text' : 'A new list item'})
        self.assertEqual(Item.objects.count(), 1) # 检查是否有一个新的Item对象存入数据库
        new_item = Item.objects.first() # 等价于object.all()[0]
        self.assertEqual(new_item.text, 'A new list item') # 检查文本是否正确

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text' : 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

class ItemModelTest(TestCase):
    def test_saving_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item' # 属性对应列，text列
        first_item.save()
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        # 得到QuerySet
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
