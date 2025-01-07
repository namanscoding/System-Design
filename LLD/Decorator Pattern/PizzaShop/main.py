from BasePizza import basePizza, Margherita,farmHouse
from PizzaToppings import Toppings, ExtraCheese

if __name__ == "__main__":
    # margherita_pizza = Margherita()
    # cheeseObj = ExtraCheese(margherita_pizza)
    #
    # print(cheeseObj.getDescrption())
    # print(cheeseObj.getPrice())

    farmhouse_pizza = farmHouse()
    cheeseObj = ExtraCheese(farmhouse_pizza)

    print(cheeseObj.getDescrption())
    print(cheeseObj.getPrice())


