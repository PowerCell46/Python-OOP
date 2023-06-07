class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'

        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += (quantity * price_per_quantity)

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'

        if ingredient not in self.ingredients.keys():
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        else:
            if quantity > self.ingredients[ingredient]:
                return f'Please check again the desired quantity of {ingredient}!'

            self.ingredients[ingredient] -= quantity
            self.price -= (quantity * price_per_quantity)

    def make_order(self):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'

        self.ordered = True
        ingredients_list = []
        for el in self.ingredients.keys():
            ingredients_list.append(f'{el}: {self.ingredients[el]}')
        ingredients_result = ", ".join(ingredients_list)
        return f'You\'ve ordered pizza {self.name} prepared with {ingredients_result} and the price will be {self.price}lv.'
