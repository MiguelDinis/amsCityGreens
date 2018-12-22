from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Favorites(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        print(self.session.keys())
        if 'favorites.id' not in self.session.keys():
            request.session['favorites.id'] = {}
        
        favs = request.session['favorites.id']

        self.favs = favs

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = self.favs.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            yield product

    def add(self, product):
        """
        Add a product to the favs
        """
        product_id = str(product.id)
        if product_id not in self.favs:
            self.favs[product_id] = 1
            self.save()

    def remove(self, product):
        """
        Remove a product from the favs.
        """
        product_id = str(product.id)
        if product_id in self.favs:
            del self.favs[product_id]
            self.save()

    def save(self):
        # update the session favs
        self.session['favorites.id'] = self.favs
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def clear(self):
        self.session['favorites.id'] = {}
        self.session.modified = True
