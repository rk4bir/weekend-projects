from django.utils.text import slugify
import random
import string
import logging

# Logger's basic configs
logging.basicConfig(
    filename='logs.txt',
    filemode='a',
    format='%(asctime)s - pid[%(process)d] - [%(levelname)s] - %(message)s',
    level=logging.INFO
)


def logger(level='INFO', request_type=None, url=None, status_code=None, message=None):
    """Takes several arguments and makes message and finally logs according to  log level."""
    message = '"%s %s [%s]" - %s' % (request_type, url, status_code, message)

    if level == 'DEBUG':
        logging.debug(message)

    if level == 'ERROR':
        logging.error(message)

    if level == 'WARNING':
        logging.warning(message)

    if level == 'INFO':
        logging.info(message)


def generate_unique_pid(instance, size=6):
    """Generate a unique code for a given instance, applicable to all model-instance
        having column `pid`
        :param instance: Any model instance having titlea and slug field
        :param size: pid size
        :return: unique slug
    """
    pid = generate_random_string(size=size, only_digit=True)

    # instance's class
    klass = instance.__class__

    # check if pid already exists
    if klass.objects.filter(pid=pid).exists():
        return generate_unique_pid(instance, size=size)

    # return the unique pid
    return pid


def generate_random_string(size=3, only_digit=False):
    """Generate a random string of length = size and return the string"""

    # return digit only
    if only_digit:
        return ''.join(random.choice(string.digits) for _ in range(size))

    # return lowercase strings only
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))


def generate_unique_slug(instance, slug=None):
    """Unique slug generator function.
        :param instance: Any model instance having titlea and slug field
        :param slug: a slugified string e.g. slugify('sample title') == sample-title
        :return: unique slug
    """

    # if no slug provided, set a slug from title
    if not slug:
        slug = slugify(instance.title)

    # instance class object
    klass = instance.__class__

    # check if slug already exists
    if klass.objects.filter(slug=slug).exists():
        new_slug = slug + '-' + generate_random_string(size=3)
        return generate_unique_slug(instance, slug=new_slug)

    # return unique slug
    return slug
