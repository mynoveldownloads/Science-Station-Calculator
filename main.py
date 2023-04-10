# Science Station Calculator


# Science station rate

placed_rate = 3.2
unplaced_rate = 3

# Budget

budget = 2000 # Number of WLS you can afford buying science stations
budget_dls = budget / 100 # Converted to DLS

buy_station_placed = budget * placed_rate # Number of placed stations you can afford
buy_station_unplaced = budget * unplaced_rate # Number of unplaced stations you can afford

print("I can buy " + str(round(buy_station_placed, )) + " placed science stations with a budget of " + str(budget) + "WLS or " + str(budget_dls) + "DLS at a rate of " + str(placed_rate) + "/WL whereas I can buy " + str(round(buy_station_unplaced, )) + " unplaced science stations with a budget of " + str(budget) + "WLS or " + str(budget_dls) + "DLS at a rate of " + str(unplaced_rate) + "/WL")

print(" ")

print("====================================================================================================")

print(" ")

# Let x be number of science station

x = 5176 # <-- Use this if you want to calculate item drop rates without calculating budget

green_eqn = (976 / 2403) * x
red_eqn = (580 / 2403) * x
yellow_eqn = (364 / 2403) * x
blue_eqn = (307 / 2403) * x
pink_eqn = (176 / 2403) * x

total_drops = green_eqn + red_eqn + yellow_eqn + blue_eqn + pink_eqn

# Price rate

green_rate = green_eqn / 200
red_rate = red_eqn / 200
yellow_rate = yellow_eqn / 70
blue_rate = blue_eqn / 200
pink_rate = pink_eqn / 200
daily_earnings = green_rate + red_rate + yellow_rate + blue_rate + pink_rate

print(str(x) + " science stations drop approximately " + str(round(green_eqn, )) + " Chemical G (" + str(round(green_rate, )) + "WLS), " + str(round(red_eqn, )) + " Chemical R (" + str(round(red_rate, )) + "WLS), " + str(round(yellow_eqn, )) + " Chemical Y (" + str(round(yellow_rate, )) + "WLS), " + str(round(blue_eqn, )) + " Chemical B (" + str(round(blue_rate, )) + "WLS) and " + str(round(pink_eqn, )) + " Chemical P (" + str(round(pink_rate, )) + "WLS), " + str(round(total_drops, )) + " drops in total with a daily earning of " + str(round(daily_earnings)) + "WLS per harvest (1 day)" )

print(" ")

print("Note: Total number of chemicals obtained = total number of science stations (1 science station always drops 1 chemical)")

print(" ")

# Return of investment

placed_price = x / placed_rate # Number of WLS paid for an x amount of placed science stations
placed_price_dls = placed_price / 100 # Converted to DLS
unplaced_price = x / unplaced_rate # Number of WLS paid for an x amount of unplaced stations
unplaced_price_dls = unplaced_price / 100 # Converted to DLS

return_wls_p = placed_price / daily_earnings # Number of days to earn WLS back buying placed science stations
return_wls_un = unplaced_price / daily_earnings # Number of days to earn WLS back buying unplaced science stations

print("It will take me about " + str(round(return_wls_p, )) + " days to earn back the number WLS in which I paid " + str(round(placed_price, )) + "WLS or "+ str(round(placed_price_dls, 2)) + "DLS for " + str(x) + " placed science stations at rate of " + str(placed_rate) + "/WL" + " whereas it will take me about " + str(round(return_wls_un, )) + " days to earn back the number WLS in which I paid " + str(round(unplaced_price, )) + "WLS or " + str(round(unplaced_price_dls, 2)) + "DLS for " + str(x) + " unplaced science stations at rate of " + str(unplaced_rate) + "/WL")

print(" ")

print("P.S: price rate of science stations and all chemicals determine the number of days you can earn your WLS back, so the number of days you can earn your WLS back will remain constant if item rate remains unchanged no matter how many WLS you spent buying x amount of science stations")

print(" ")
