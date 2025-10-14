# Lemonade Stand
# Written and tested with Python 3.11.2
# nilten.neocities.org

import random
import math

# Global variables
global sys_gameState
sys_gameState = None

global player_name
global player_dayCount
global player_money
global player_spendings

player_name = "Missingno."
player_dayCount = 0
player_money = 5 # player starts with 10 bucks
player_spendings = 0

global dayCycle_playerLemonade
global dayCycle_playerSugar
global dayCycle_playerAdverts

dayCycle_playerLemonade = int(0)
dayCycle_playerPrice = float(0)
dayCycle_playerSugar = int(0)
dayCycle_playerAdverts = int(0)

global dayCycle_priceLemonade
global dayCycle_priceSugar
global dayCycle_priceAdverts

dayCycle_priceLemonade = 0.05
dayCycle_priceSugar = 0.08
dayCycle_priceAdverts = 0.20


def func_initPlayerVar():
    global player_name
    global player_dayCount
    global player_money
    global player_spendings

    player_name = "N/A"
    player_dayCount = 0
    player_money = 5
    player_spendings = 0

def func_initDayCycleVar():
    global dayCycle_playerLemonade
    global dayCycle_playerSugar
    global dayCycle_playerAdverts
    global player_spendings

    dayCycle_playerLemonade = 0
    dayCycle_playerSugar = 0
    dayCycle_playerAdverts = 0
    player_spendings

def func_checkPlayerBrokeness(spendings): # love that name btw lmao
    global player_money
    global player_name
    if spendings > math.floor(player_money * 100) / 100:
        print(f"You don't have enough money to do that, {player_name}!")

def func_gameState(gameState):
    global sys_gameState

    if gameState == "TitleScreen":
        sys_gameState = "TitleScreen"
        func_titleScreen()
    elif gameState == "DayStart":
        sys_gameState = "DayStart"
        func_gameLoop()
    elif gameState == "MakeLemonade":
        sys_gameState = "MakeLemonade"
    elif gameState == "AddSugar":
        sys_gameState = "AddSugar"
    elif gameState == "MakeAds":
        sys_gameState = "MakeAds"
    elif gameState == "GameQuit":
        sys_gameState = "GameQuit"
        print("See ya!")
    else:
        #print("Warning: No valid game state found !")
        #print("Restarting game...")

        # init all global variables and restart on title screen
        func_initPlayerVar()
        func_initDayCycleVar()
        sys_gameState = "TitleScreen"
        func_titleScreen()

def func_titleScreen():
    global player_name
    # init global variables on game start
    func_initPlayerVar()
    func_initDayCycleVar()

    print("Welcome to Lemonade Stand!")
    print("Please enter your name: ")
    player_name = str(input())
    print(f"Welcome, {player_name}!")
    func_gameState("DayStart")

def func_gameLoop():
    global player_dayCount
    global player_money
    global player_spendings
    func_initDayCycleVar()
    player_dayCount += 1
    print(f"Day {player_dayCount}")
    print("It's a sunny day!")
    print(f"Your balance is {player_money} bucks.")

    func_gameState("MakeLemonade")
#   print(sys_gameState)
    while dayCycle_playerLemonade <= 0:
        func_playerMakeLemonade()
        while player_spendings > player_money:
            func_playerMakeLemonade()
    func_playerDefinePrice()

    func_gameState("AddSugar")
#   print(sys_gameState)
    func_playerAddSugar()

    func_gameState("MakeAds")
#   print(sys_gameState)
    func_playerMakeAds()

    func_calcDayResults()

def func_playerMakeLemonade():
    global player_name
    global player_money
    global player_spendings
    global dayCycle_playerLemonade
    global dayCycle_priceLemonade

    print(f"{player_name}, How much Lemonade would you like to make today? ")
    print(f"Costs per glass of lemonade: {dayCycle_priceLemonade} bucks.")
    print(f"You have {player_money} bucks.")
    dayCycle_playerLemonade = int(input())
    player_spendings = math.floor((dayCycle_playerLemonade * dayCycle_priceLemonade) * 100) / 100
    if dayCycle_playerLemonade <= 0:
        print("How are you going to sell anything without any lemonade?")
        return   # Loop back to start
    elif player_spendings > player_money:
        print(f"You don't have enough money to make that much lemonade, {player_name}!")
        return # Loop back to start
    else:
        player_money = player_money - (float(dayCycle_playerLemonade) * dayCycle_priceLemonade)
        math.floor(player_money * 100) / 100
        int(dayCycle_playerLemonade)
        print(f"You've made {dayCycle_playerLemonade} glasses of Lemonade!")
        print(f"You have {player_money} bucks left.")

def func_playerDefinePrice():
    global player_name
    global dayCycle_playerPrice    

    print(f"{player_name}, how much money would you like to charge for your lemonade?")
    dayCycle_playerPrice = float(input())
    if dayCycle_playerPrice >= 3.0:
        print(f"You decided to charge your lemonade for {dayCycle_playerPrice} buc- {dayCycle_playerPrice} BUCKS?! ...that's quite steep, don't you think?")
    else:
        print(f"You decided to charge your lemonade for {dayCycle_playerPrice} bucks!")

def func_playerAddSugar():
    global player_name
    global player_money
    global player_spendings
    global dayCycle_playerSugar
    global dayCycle_priceSugar

    print(f"{player_name}, How many grams of sugar would you like to add to your lemonade? ")
    print(f"Costs per gram of sugar: {dayCycle_priceSugar} bucks.")
    print(f"You have {player_money} bucks.")
    dayCycle_playerSugar = int(input())
    player_spendings = math.floor((dayCycle_playerLemonade * dayCycle_priceLemonade) * 100) / 100
    if dayCycle_playerSugar == 0:
        print("Au' naturel? Your choice!") # No loop needed
    elif player_spendings > player_money:
        print(f"You don't have enough money for that amount of sugar, {player_name}!")
        return
    elif dayCycle_playerSugar >= 50:
        print("That's quite a lot! You'll give your customers a sugar rush!")
        player_money = player_money - (float(dayCycle_playerSugar) * dayCycle_priceSugar)
        math.floor(player_money * 100) / 100
        int(dayCycle_playerSugar)
        print(f"You've added {dayCycle_playerSugar} grams of Sugar to your lemonade!")
        print(f"You have {player_money} bucks left.")
    else:
        player_money = player_money - (float(dayCycle_playerSugar) * dayCycle_priceSugar)
        math.floor(player_money * 100) / 100
        int(dayCycle_playerSugar)
        print(f"You've added {dayCycle_playerSugar} grams of Sugar to your lemonade!")
        print(f"You have {player_money} bucks left.")

def func_playerMakeAds():
    global player_name
    global player_money
    global player_spendings
    global dayCycle_playerAdverts
    global dayCycle_priceAdverts

    print(f"{player_name}, How many advertisements would you like to put up? ")
    print(f"Costs per advertisement: {dayCycle_priceAdverts} bucks.")
    print(f"You have {player_money} bucks.")
    dayCycle_playerAdverts = int(input())
    player_spendings = math.floor((dayCycle_playerLemonade * dayCycle_priceLemonade) * 100) / 100
    if dayCycle_playerAdverts == 0:
        print("No Ads? Your choice!") # No loop needed
    elif player_spendings > player_money:
        print(f"You don't have enough money for that many ad spaces, {player_name}!")
        return
    else:
        player_money = player_money - (float(dayCycle_playerAdverts) * dayCycle_priceAdverts)
        math.floor(player_money * 100) / 100
        int(dayCycle_playerAdverts)
        print(f"You've put up {dayCycle_playerAdverts} adverts around your town!")
        print(f"You have {player_money} bucks left.")

def func_calcDayResults():
    global player_name
    global player_money
    global player_dayCount
    global dayCycle_playerLemonade
    global dayCycle_playerPrice
    global dayCycle_playerSugar
    global dayCycle_playerAdverts

    dayCycle_playerProfit = 0
    customerMultiplier = 0
    customers = 0

    if dayCycle_playerPrice <= 0.75:
        customerMultiplier = customerMultiplier + random.uniform((dayCycle_playerLemonade/1.5), dayCycle_playerLemonade)
    elif dayCycle_playerPrice <= 2:
        customerMultiplier = customerMultiplier + random.uniform((dayCycle_playerLemonade/3), dayCycle_playerLemonade)
    elif dayCycle_playerPrice <= 5:
        customerMultiplier = customerMultiplier + random.uniform((dayCycle_playerLemonade/5), dayCycle_playerLemonade/2)
    else:
        customerMultiplier = customerMultiplier + random.uniform((dayCycle_playerLemonade/6), (dayCycle_playerLemonade/4.5))
    
    int(dayCycle_playerLemonade)

    if dayCycle_playerSugar <= 5:
        customerMultiplier = customerMultiplier - random.uniform((dayCycle_playerSugar/2), (dayCycle_playerSugar/1.5))
    elif dayCycle_playerSugar <= 30:
        customerMultiplier = customerMultiplier + random.uniform((dayCycle_playerSugar/1.5), dayCycle_playerSugar)
    elif dayCycle_playerSugar > 30:
        customerMultiplier = customerMultiplier - random.uniform((dayCycle_playerSugar/2), (dayCycle_playerSugar/1.5))

    int(dayCycle_playerSugar)

#   print(customerMultiplier)

    if customerMultiplier < 0:
        customerMultiplier = 0

    customers = int(math.floor(customerMultiplier * 100) / 100)

    if customers < dayCycle_playerLemonade:
        customers = dayCycle_playerLemonade

    dayCycle_playerProfit = customers * dayCycle_playerPrice

    player_money = player_money + dayCycle_playerProfit

    print("*DAILY REPORT*")
    print(f"Glasses of lemonade produced: {dayCycle_playerLemonade}")
    print(f"Amounts of sugar used per glass: {dayCycle_playerSugar}")
    print(f"Amount of ads booked today: {dayCycle_playerAdverts}")
    print(f"Amount of lemonade sold: {customers} out of {dayCycle_playerLemonade}")
    print(f"Today's profit: {dayCycle_playerProfit}")
    print(f"Your balance: {player_money}")

    if player_money <= 0:
        print(f"BREAKING NEWS: {player_name} calls it quits !")
        print("You've ran out of pocket money !")
        print("Game Over !")
        print(f"You've made it to Day {player_dayCount}")
        input("Press any key to return to the Title Screen...")
        func_gameState("TitleScreen")
    else:
        input(f"Press any key to continue with day {player_dayCount+1}...")
        func_gameLoop() # Reset loop

# Program loop
if sys_gameState != "GameQuit":
    func_gameState(sys_gameState)
else:
    func_gameState("GameQuit")
