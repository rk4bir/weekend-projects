from django.db import models
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# generate_unique_slug(instance, slug=None)
# generate_unique_slug(instance, size=6)
from .utils import generate_unique_slug, generate_unique_pid


class Size(models.Model):
    """Size model/table: Size model is related to Product model in Generic fashion"""
    # size name: e.g. 'M'
    title = models.CharField(max_length=6, blank=False, null=False)
    description = models.TextField()

    # Generic relation to Product table/model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="available_sizes")
    object_id = models.CharField(max_length=30)
    content_object = GenericForeignKey('content_type', 'object_id')

    # creation & updated timestamp
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.description)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class Color(models.Model):
    """Color model/table: Color model is related to Product model in Generic fashion"""
    # color name: e.g. 'blue'
    title = models.CharField(max_length=12, blank=False, null=False)

    # color code: for hex, rgb color code
    color_code = models.CharField(max_length=20, blank=True, null=True)

    # Generic relation to Product table/model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="available_colors")
    object_id = models.CharField(max_length=30)
    content_object = GenericForeignKey('content_type', 'object_id')

    # creation & updated timestamp
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.color_code)


class Price(models.Model):
    """Price model/table: Price model is related to Product model in Generic fashion"""
    price = models.FloatField(blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)

    # Generic relation to Price table/model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="prices")
    object_id = models.CharField(max_length=30)
    content_object = GenericForeignKey('content_type', 'object_id')

    # creation & updated timestamp
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.price) + ': ' + str(self.start_date) + ' to ' + str(self.end_date)


class Product(models.Model):
    """ Database model for products.
        columns: id, pk, title, slug, pid, in_stock, stocks, price, created, updated
        Product is related to Size, Color and Price table with Generic relations. So,
        it'll simplify the relation complexity. e.g. to call all prices along with date
        range one will use:
            instance.prices.all()
    """
    title = models.CharField(max_length=100, blank=False, null=False)

    # unique slug will be generated automatically from title
    slug = models.SlugField(blank=True, null=True, unique=True)

    # product identifier
    pid = models.CharField(max_length=20, blank=True, null=True)

    # generic relations to Size, Color and Price table/model
    sizes = GenericRelation(Size)
    colors = GenericRelation(Color)
    prices = GenericRelation(Price)

    # stock, count & price
    in_stock = models.BooleanField(default=False)
    stocks = models.PositiveIntegerField(default=0)

    # creation & updated timestamp
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-created']

    # model string
    def __str__(self):
        return "%s: %s" % (self.title, self.stocks)

    # property: stock status => available or not available
    @property
    def stock_status(self):
        """Validate availability of the product"""
        if self.stocks > 0:
            self.in_stock = True
        else:
            self.in_stock = False
        self.save()
        return 'Available' if self.in_stock else 'Not available'

    # property: comma separated sizes
    @property
    def available_sizes(self):
        sizes = self.sizes.all()
        return ', '.join(size.title for size in sizes)

    # property: comma separated colors
    @property
    def available_colors(self):
        colors = self.colors.all()
        return ', '.join(color.title for color in colors)

    # property: prices list
    def price_ranges(self):
        prices = self.prices.all()
        return [{'price': price.price, 'start_date': price.start_date, 'end_date': price.end_date}
                    for price in prices]


# Product after save action: set slug and pid
def product_pre_save_action(sender, instance, *args, **kwargs):
    """Sets slug and pid when a model instance is being saved.
        This function automatically executes when a instance.save()
        is called.
    """
    # set slug if note provided
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)

    # set pid if not provided
    if not instance.pid:
        instance.pid = generate_unique_pid(instance)


# Note also that Django stores signal handlers as weak references by default,
# so if your handler is a local function, it may be garbage collected.
# To prevent this, pass weak=False when you call the signal’s connect().
# ref: https://docs.djangoproject.com/en/2.2/ref/signals/
pre_save.connect(product_pre_save_action, sender=Product, weak=False)
