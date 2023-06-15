
class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for el in self.products:
            if el.name == product_name:
                return el

    def remove(self, product_name):
        for index in range(len(self.products)):
            current_product = self.products[index]
            if current_product.name == product_name:
                self.products.pop(index)
                break

    def __repr__(self):
        return_list = []
        for el in self.products:
            return_list.append(f'{el.name}: {el.quantity}')
        return "\n".join(return_list)
