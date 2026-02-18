# Lemonade Stand
# Written and tested with Python 3.11.2
# nilten.neocities.org

import random
import math

# Global variables
global sys_state
sys_state = None

global player_name
global player_dayCount
global player_money
global player_expenditures

player_name = "Missingno."
player_dayCount = 0
player_money = 5                    # player starts with 10 bucks
player_expenditures = 0

global day_cycle_player_lemonade
global day_cycle_player_sugar
global day_cycle_playerAdverts

day_cycle_player_lemonade = int(0)
day_cycle_playerPrice = float(0)
day_cycle_player_sugar = int(0)
day_cycle_playerAdverts = int(0)

global day_cycle_price_lemonade
global day_cycle_price_sugar
global day_cycle_priceAdverts

day_cycle_price_lemonade = 0.05
day_cycle_price_sugar = 0.08
day_cycle_priceAdverts = 0.20


def init_player_var():
    global player_name
    global player_dayCount
    global player_money
    global player_expenditures

    player_name = "N/A"
    player_dayCount = 0
    player_money = 5
    player_expenditures = 0


def init_day_cycle():
    global day_cycle_player_lemonade
    global day_cycle_player_sugar
    global day_cycle_playerAdverts
    global player_expenditures

    day_cycle_player_lemonade = 0
    day_cycle_player_sugar = 0
    day_cycle_playerAdverts = 0
    player_expenditures = 0


def check_player_brokeness(expenditures):            # love that name btw lmao
    global player_money
    global player_name
    if expenditures > math.floor(player_money * 100) / 100:
        print(f"You don't have enough money to do that, {player_name}!")


def game_state(state):
    global sys_state

    if state == "TitleScreen":
        sys_state = "TitleScreen"
        title_screen()
    elif state == "DayStart":
        sys_state = "DayStart"
        game_loop()
    elif state == "MakeLemonade":
        sys_state = "MakeLemonade"
    elif state == "AddSugar":
        sys_state = "AddSugar"
    elif state == "MakeAds":
        sys_state = "MakeAds"
    elif state == "GameQuit":
        sys_state = "GameQuit"
        print("See ya!")
    else:
        # init all global variables and restart on title screen
        init_player_var()
        init_day_cycle()
        sys_state = "TitleScreen"
        title_screen()


def title_screen():
    global player_name
    # init global variables on game start
    init_player_var()
    init_day_cycle()

    print("Welcome to Lemonade Stand!")
    print("Please enter your name: ")
    player_name = str(input())
    print(f"Welcome, {player_name}!")
    game_state("DayStart")


def game_loop():
    global player_dayCount
    global player_money
    global player_expenditures
    init_day_cycle()
    player_dayCount += 1
    print(f"Day {player_dayCount}")
    print("It's a sunny day!")
    print(f"Your balance is {player_money} bucks.")

    game_state("MakeLemonade")
#   print(sys_state)
    while day_cycle_player_lemonade <= 0:
        player_make_lemonade()
        while player_expenditures > player_money:
            player_make_lemonade()
    player_define_price()

    game_state("AddSugar")
#   print(sys_state)
    player_add_sugar()

    game_state("MakeAds")
#   print(sys_state)
    player_make_ads()

    calc_day_results()


def player_make_lemonade():
    global player_name
    global player_money
    global player_expenditures
    global day_cycle_player_lemonade
    global day_cycle_price_lemonade

    print(f"{player_name}, How much Lemonade would you like to make today? ")
    print(f"Costs per glass of lemonade: {day_cycle_price_lemonade} bucks.")
    print(f"You have {player_money} bucks.")
    day_cycle_player_lemonade = int(input())
    player_expenditures = math.floor((day_cycle_player_lemonade * day_cycle_price_lemonade) * 100) / 100
    if day_cycle_player_lemonade <= 0:
        print("How are you going to sell anything without any lemonade?")
        # Loop back to start
    elif player_expenditures > player_money:
        print(f"You don't have enough money to make that much lemonade, {player_name}!")
        # Loop back to start
    else:
        player_money = player_money - (float(day_cycle_player_lemonade) * day_cycle_price_lemonade)
        player_money = math.floor(player_money * 100) / 100
        int(day_cycle_player_lemonade)
        print(f"You've made {day_cycle_player_lemonade} glasses of Lemonade!")
        print(f"You have {player_money} bucks left.")


def player_define_price():
    global player_name
    global day_cycle_playerPrice

    print(f"{player_name}, how much money would you like to charge for your lemonade?")
    day_cycle_playerPrice = float(input())
    if day_cycle_playerPrice >= 3.0:
        print(f"You decided to charge your lemonade for {day_cycle_playerPrice} buc- {day_cycle_playerPrice} BUCKS?! \
                ...that's quite steep, don't you think?")
    else:
        print(f"You decided to charge your lemonade for {day_cycle_playerPrice} bucks!")


def player_add_sugar():
    global player_name
    global player_money
    global player_expenditures
    global day_cycle_player_sugar
    global day_cycle_price_sugar

    print(f"{player_name}, How many grams of sugar would you like to add to your lemonade? ")
    print(f"Costs per gram of sugar: {day_cycle_price_sugar} bucks.")
    print(f"You have {player_money} bucks.")
    day_cycle_player_sugar = int(input())
    player_expenditures = math.floor((day_cycle_player_lemonade * day_cycle_price_lemonade) * 100) / 100
    if day_cycle_player_sugar == 0:
        print("Au' naturel? Your choice!")              # No loop needed
    elif player_expenditures > player_money:
        print(f"You don't have enough money for that amount of sugar, {player_name}!")
    elif day_cycle_player_sugar >= 50:
        print("That's quite a lot! You'll give your customers a sugar rush!")
        player_money = player_money - (float(day_cycle_player_sugar) * day_cycle_price_sugar)
        player_money = math.floor(player_money * 100) / 100
        int(day_cycle_player_sugar)
        print(f"You've added {day_cycle_player_sugar} grams of Sugar to your lemonade!")
        print(f"You have {player_money} bucks left.")
    else:
        player_money = player_money - (float(day_cycle_player_sugar) * day_cycle_price_sugar)
        player_money = math.floor(player_money * 100) / 100
        int(day_cycle_player_sugar)
        print(f"You've added {day_cycle_player_sugar} grams of Sugar to your lemonade!")
        print(f"You have {player_money} bucks left.")


def player_make_ads():
    global player_name
    global player_money
    global player_expenditures
    global day_cycle_playerAdverts
    global day_cycle_priceAdverts

    print(f"{player_name}, How many advertisements would you like to put up? ")
    print(f"Costs per advertisement: {day_cycle_priceAdverts} bucks.")
    print(f"You have {player_money} bucks.")
    day_cycle_playerAdverts = int(input())
    player_expenditures = math.floor((day_cycle_player_lemonade * day_cycle_price_lemonade) * 100) / 100
    if day_cycle_playerAdverts == 0:
        print("No Ads? Your choice!")               # No loop needed
    elif player_expenditures > player_money:
        print(f"You don't have enough money for that many ad spaces, {player_name}!")
    else:
        player_money = player_money - (float(day_cycle_playerAdverts) * day_cycle_priceAdverts)
        player_money = math.floor(player_money * 100) / 100
        int(day_cycle_playerAdverts)
        print(f"You've put up {day_cycle_playerAdverts} adverts around your town!")
        print(f"You have {player_money} bucks left.")


def calc_day_results():
    global player_name
    global player_money
    global player_dayCount
    global day_cycle_player_lemonade
    global day_cycle_playerPrice
    global day_cycle_player_sugar
    global day_cycle_playerAdverts

    day_cycle_player_profit = 0
    customer_multiplier = 0
    customers = 0

    if day_cycle_playerPrice <= 0.75:
        customer_multiplier = customer_multiplier + random.uniform((day_cycle_player_lemonade/1.5), day_cycle_player_lemonade)
    elif day_cycle_playerPrice <= 2:
        customer_multiplier = customer_multiplier + random.uniform((day_cycle_player_lemonade/3), day_cycle_player_lemonade)
    elif day_cycle_playerPrice <= 5:
        customer_multiplier = customer_multiplier + random.uniform((day_cycle_player_lemonade/5), day_cycle_player_lemonade/2)
    else:
        customer_multiplier = customer_multiplier + random.uniform((day_cycle_player_lemonade/6), (day_cycle_player_lemonade/4.5))

    int(day_cycle_player_lemonade)

    if day_cycle_player_sugar <= 5:
        customer_multiplier = customer_multiplier - random.uniform((day_cycle_player_sugar/2), (day_cycle_player_sugar/1.5))
    elif day_cycle_player_sugar <= 30:
        customer_multiplier = customer_multiplier + random.uniform((day_cycle_player_sugar/1.5), day_cycle_player_sugar)
    elif day_cycle_player_sugar > 30:
        customer_multiplier = customer_multiplier - random.uniform((day_cycle_player_sugar/2), (day_cycle_player_sugar/1.5))

    int(day_cycle_player_sugar)

#   print(customer_multiplier)

    if customer_multiplier < 0:
        customer_multiplier = 0

    customers = int(math.floor(customer_multiplier * 100) / 100)

    if customers < day_cycle_player_lemonade:
        customers = day_cycle_player_lemonade

    day_cycle_player_profit = customers * day_cycle_playerPrice

    player_money = player_money + day_cycle_player_profit

    print("*DAILY REPORT*")
    print(f"Glasses of lemonade produced: {day_cycle_player_lemonade}")
    print(f"Amounts of sugar used per glass: {day_cycle_player_sugar}")
    print(f"Amount of ads booked today: {day_cycle_playerAdverts}")
    print(f"Amount of lemonade sold: {customers} out of {day_cycle_player_lemonade}")
    print(f"Today's profit: {day_cycle_player_profit}")
    print(f"Your balance: {player_money}")

    if player_money <= 0:
        print(f"BREAKING NEWS: {player_name} calls it quits !")
        print("You've ran out of pocket money !")
        print("Game Over !")
        print(f"You've made it to Day {player_dayCount}")
        input("Press any key to return to the Title Screen...")
        game_state("TitleScreen")
    else:
        input(f"Press any key to continue with day {player_dayCount+1}...")
        game_loop()             # Reset loop


# Program loop
if sys_state != "GameQuit":
    game_state(sys_state)
else:
    game_state("GameQuit")
