"""Classes for melon orders."""
import random
import datetime

class AbstractMelonOrder:
    """ an abstracct base class that other Melon Orders inherit from"""

    def __init__(self, species, qty, ordertype):

        self.species = species
        self.qty = qty
        if qty>100:
            raise TooManyMelonsError
        self.shipped = False
        self.tax = 0 #this line can be self.tax = tax if tax is passed as an argument in the init method
        self.order_type = ordertype
     
    
    def mark_shipped(self):
        self.shipped = True

    def get_base_price(self):

        base_price = random.randint(5,9)

        now = datetime.datetime.now()
        if now.hour>8 and now.hour<11:
            base_price += 4

        return base_price
    
    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price
        if self.species == "Christmas melon":
            base_price = base_price*1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty <10:
            total += 3

        return total
    


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    #the base class needs to pass in all the arguments from the parents' class init function
    #however, base class can add more arguments specific to the base class if only its defined inside the base class's init function
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty,"domestic")
        #alternative super().__init__(species, qty,"domestic",0.08) to do this, tax needed to be passed as an argument in the parent class
        # self.order_type = "domestic" this line can be replaced by passing "domestic" in the super().__init__method
        self.tax = 0.08 #this line can possibly be replaced by passing a number in the super().__init__method


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code): #can take in additional arguments not in parent class but will need to define it (eg. country_code)
        """Initialize melon order attributes."""
        super().__init__(species, qty,"international") #pass in the necessary arguments for parent class 
        self.country_code = country_code
        # self.order_type = "international" this line can be replaced by passing "domestic" in the super().__init__method
        self.tax = 0.17 #this line can possibly be replaced by passing a number in the super().__init__method

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty,"government")

        self.pass_inspection = False #this is equivalent to def __init__(self, species, qty, pass_inspection=False)
     
    def mark_inspection(self,passed):
        self.pass_inspection = passed

class TooManyMelonsError(ValueError):

    def __init__(self):
        super().__init__("Too many melons")