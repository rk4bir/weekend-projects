from django.test import TestCase
from products.models import Size, Color, Price, Product


class ModelTests(TestCase):

    def setUp(self):
        # product instances
        self.panjabi = Product.objects.create(title="Panjabi")
        self.lungi = Product.objects.create(title="Lungi", in_stock=True, stocks=10)

        # size instances
        self.m_size = Size.objects.create(title='M', description='Medium', content_object=self.panjabi)
        self.l_size = Size.objects.create(title='L', description='Long', content_object=self.panjabi)

        # color instances
        self.lungi_black = Color.objects.create(title='Black', color_code='#000000', content_object=self.lungi)
        self.lungi_blue = Color.objects.create(title='Black', color_code='#003390', content_object=self.lungi)

        # price instances: date is YYYY/MM/DD required
        self.panjabi_price1 = Price.objects.create(price=1290.00,
                                                   start_date='2019-12-5',
                                                   end_date='2019-12-10',
                                                   content_object=self.panjabi)

        self.panjabi_price2 = Price.objects.create(price=1390.00,
                                                   start_date='2019-12-11',
                                                   end_date='2019-12-20',
                                                   content_object=self.panjabi)

    def test_product_stock_status_property(self):
        '''Testing stock_status property'''
        self.assertEqual(self.panjabi.stock_status, "Not available")
        self.assertEqual(self.lungi.stock_status, "Available")

    def test_generic_relations_for_product_model(self):
        '''Testing replies, colors & prices attribute for product instance'''
        self.assertEquals(list(self.lungi.colors.all()), [self.lungi_black, self.lungi_blue])
        self.assertEquals(list(self.panjabi.sizes.all()), [self.m_size, self.l_size])
        self.assertEquals(list(self.panjabi.prices.all()), [self.panjabi_price1, self.panjabi_price2])
