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

    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest() # 创建一个HTTPRequest对象
    #     response = home_page(request) # 传给home_page视图，得到响应
    #     html = response.content.decode('utf8') # 提取content，得到原始字节
    #     expected_html = render_to_string('home.html')
    #     self.assertEqual(html, expected_html)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text' : 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

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
