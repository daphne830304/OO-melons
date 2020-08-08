"""Classes for melon orders."""

class AbstractMelonOrder:
    """ an abstracct base class that other Melon Orders inherit from"""

    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0
        self.order_type = None
     
    
    def mark_shipped(self):
        self.shipped = True
    
    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == "Christmas melon":
            base_price = base_price*1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty <10:
            total += 3

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""
    #     super().get_total()


    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""
    #     super().mark_shipped()


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

        

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""
    #     super().mark_shipped()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty, pass_inspection=False):#,mark_inspection):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        self.pass_inspection = pass_inspection
        # self.mark_inspection = 
    def mark_inspection(self,passed):
        self.pass_inspection = passed
