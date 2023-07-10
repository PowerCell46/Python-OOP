class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id):
        for dvd in self.dvds:

            if dvd.id == dvd_id:

                current_customer = None
                for person in self.customers:
                    if person.id == customer_id:
                        current_customer = person

                if dvd.is_rented == False:

                    if current_customer.age < dvd.age_restriction:
                        return f'{current_customer.name} should be at least {dvd.age_restriction} to rent this movie'
                    else:
                        dvd.is_rented = True
                        current_customer.rented_dvds.append(dvd)
                        return f'{current_customer.name} has successfully rented {dvd.name}'

                else:
                    if dvd in current_customer.rented_dvds:
                        return f'{current_customer.name} has already rented {dvd.name}'
                    else:
                        return f'DVD is already rented'

    def return_dvd(self, customer_id, dvd_id):
        current_customer = None
        for person in self.customers:
            if person.id == customer_id:
                current_customer = person
                for index in range(len(current_customer.rented_dvds)):
                    dvd = current_customer.rented_dvds[index]
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        current_customer.rented_dvds.pop(index)
                        for dvd in self.dvds:
                            if dvd.id == dvd_id:
                                dvd.is_rented = False
                                return f'{current_customer.name} has successfully returned {dvd.name}'

        return f'{current_customer.name} does not have that DVD'

    def __repr__(self):
        return_list = []

        index = 0
        for person in self.customers:
            index += 1
            return_list.append(f'{person}')

        index = 0
        for dvd in self.dvds:
            index += 1
            return_list.append(f'{dvd}')

        return "\n".join(return_list)
