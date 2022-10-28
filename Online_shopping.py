"""This is a mock exercise of building a shopping cart and writing reviews. although tough to code at first, most of the code was simple due to examples given.
much of this answer is the same as the given solution besides variable names because the way we coded it was similar but there strategy was more clear."""

#  Basic class that will be inhereted but can operate on its own with its own variable to be stored
class Product:
    def __init__(self, name, description, seller, price, available):
        self.name = name
        self.description = description
        self.seller = seller
        self.reviews = []
        self.price = price
        self.available = available

    def __str__(self):
        return f"Product({self.name}, {self.description}) at ${self.price}"
      
#  Basic class that will be inhereted but can operate on its own with its own variable to be stored
#  This class also needs to be called when a review is written
class Review:
    def __init__(self, content, user, product):
        self.content = content
        self.user = user
        self.product = product

    def __str__(self):
        return f"Review of {self.product} by {self.user}: '{self.content}'"

      
""" Originally when i got stuck, i didn't realize to inhereit all the classes to the user,
until it was obvious that the user was controlling most of the actions in the example. good reminder."""
class User(Review,Product):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []

    def write_review(self, content, product):
        review = Review(content, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        print(f"{self.name}'s review of {product.name}: {review.content}")
        return review

    def sell_product(self, name, description, price):
        product = Product(name, description, price, self, available=True)
        print(f"{product} is on the market!")
        return product

    def buy_product(self, product):
        if product.available:
            print(f"{self} is buying {product}.")
            product.available = False
        else:
            print(f"{product} is no longer available.")

    def __str__(self):
        return f"User(id={self.id}, name={self.name})"
