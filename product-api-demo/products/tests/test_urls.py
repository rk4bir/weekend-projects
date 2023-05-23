from django.test import TestCase, Client
from ..models import Product


class UrlTests(TestCase):

    def setUp(self):
        self.browser = Client(enforce_csrf_checks=True, HTTP_USER_AGENT='Mozilla/5.0')
        self.product = Product.objects.create(title='Shari', in_stock=True, stocks=10)

        # product requests
        self.product_list_req = self.browser.get('/products/')
        self.product_detail_req = self.browser.get('/products/shari/')

        # sizes, colors, price reqeusts
        self.size_req = self.browser.post(
                            '/products/' + self.product.slug + '/size/',
                            {'title': 'M', 'description': "Medium"})

        self.color_req = self.browser.post(
                                '/products/' + self.product.slug + '/color/',
                                {'title': 'black', 'color_code': '#000000'})
        self.price_req = self.browser.post(
                                '/products/' + self.product.slug + '/price/',
                                {'price': 3000.0, 'start_date': '2019-12-2', 'end_date': '2019-12-10'})

    def test_product_urls(self):
        """As a GET request the response status should be 200"""
        self.assertEquals(self.product_list_req.status_code, 200)
        self.assertEquals(self.product_detail_req.status_code, 200)

    def test_attribute_setting_urls(self):
        """As a POST request the response status should be 201"""
        self.assertEquals(self.size_req.status_code, 201)
        self.assertEquals(self.color_req.status_code, 201)
        self.assertEquals(self.price_req.status_code, 201)
