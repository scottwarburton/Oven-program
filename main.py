# Oven program

class Oven:

    def __init__(self, power, water, soap):
        self.power = power
        self.water = water
        self.soap = soap

    def cook(self, dish):
        global cycles
        global error_message
        global power
        global water
        global soap
        global error_message
        if self.system_checks() == True:
            if dish == 1:
                print("Your roast has now cooked")
            elif dish == 2:
                print("Your pies have now cooked")
            elif dish == 3:
                print("Your cake has now baked")
        else:
            print(error_message)
            print("Please recharge or clean from the main menu")

        error_message = ""
        self.power -= 10
        global cycles
        cycles += 1

    def recharge(self):
        self.power += 100
        if self.power >= 300:
            print("The oven is now on fire")

        else:
            print("The oven is now recharged")

    def clean(self):
        global cycles
        if self.water >= 1 and self.soap >= 1:
            self.water -= 1
            self.soap -= 1
            cycles = 0
            return True
        else:
            return False

    def resupply(self):
        self.water += 5
        self.soap += 5
        print("The oven is now resupplied")

    def show_levels(self):
        print(str(self.power) + " of power")
        print(str(self.water) + " of water")
        print(str(self.soap) + " of soap")

    def system_checks(self):
        global error_message
        global cycles
        error_message = ""
        if self.power <= 20 and cycles >= 3:
            error_message = "Not enough power and clean needed"
            return False
        elif self.power <= 20 and cycles < 3:
            error_message = "Not enough power"
            return False
        elif self.power > 20 and cycles >= 3:
            error_message = "Clean needed"
            return False
        else:
            return True

    def main(self):
        global cycles
        cycles = 0

        while True:
            oven_menu = int(input(
                "\nPress 1 to cook, 2 to recharge, 3 to clean, 4 to resupply, 5 to show levels, or 6 to shutdown:\n > "))

            if oven_menu == 1:
                while True:
                    dish_chosen = int(
                        input("\nPress 1 for roast, 2 for pies, 3 for cake, or 4 to return to the oven menu:\n > "))
                    if dish_chosen == 4:
                        break
                    elif dish_chosen == 1 or 2 or 3:
                        self.cook(dish_chosen)

                    else:
                        print("invalid dish selection")
                        continue
            elif oven_menu == 2:
                self.recharge()
            elif oven_menu == 3:
                if self.clean() == True:
                    print("The oven is now clean")
                else:
                    print("Resupply needed before cleaning")
            elif oven_menu == 4:
                self.resupply()
            elif oven_menu == 5:
                self.show_levels()
            elif oven_menu == 6:
                print("Goodbye")
                break
            else:
                print("invalid menu selection")
                continue


MyOven = Oven(100, 5, 5)
MyOven.main()

# end