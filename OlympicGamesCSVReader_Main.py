# Main file for OlympicGamesCSVReader

# Import functions
from OlympicGamesCSVReader_Functions import *

# Testing totalMedalsByCountry function through USA
print(totalMedalsByCountry('USA'))

# Testing countriesWithMedalInSport function through Aquatics
print(countriesWithMedalInSport('Aquatics'))

# Testing goldMedalsByCountryAndYears function through gold medals of USA in 2012
print(goldMedalsByCountryAndYears('USA', 2012))