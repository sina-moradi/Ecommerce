import string
import random


def random_generate(size=26, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_slug(model, length=6):
    """
    generate slug for model.

    :param type model: the model class.
    :param int length: length of generated slug.

    :rtype: str
    """

    slug = random_generate(length)
    existed = model.objects.filter(slug=slug).exists()
    if existed is True:
        return generate_slug(model)

    return slug