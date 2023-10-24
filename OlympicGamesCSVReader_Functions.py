# This project aims to cover collection types/collection object methods, reading information from CSV files, and text processing in
# Python. The CSV files include one providing country codes and another providing information regarding the Summer Olympic Games.

# Imports
import csv

# Returns the total number of each medal type won by the specified country
def totalMedalsByCountry(code = 'ALL'):
    with open('summer.csv', 'r', encoding = "utf8") as medalFile:
        medals = csv.reader(medalFile)
        totalGold = []
        totalSilver = []
        totalBronze = []
        for level in medals:
            if code == 'ALL':
                if level[8] == 'Gold':
                    totalGold.append(level[8])
                elif level[8] == 'Silver':
                    totalSilver.append(level[8])
                else:
                    totalBronze.append(level[8])
            elif code == level[5]:
                if level[8] == 'Gold':
                    totalGold.append(level[8])
                elif level[8] == 'Silver':
                    totalSilver.append(level[8])
                else:
                    totalBronze.append(level[8])
    totalMedals = {'Gold': totalGold.count('Gold'), 'Silver': totalSilver.count('Silver'), 'Bronze': totalBronze.count('Bronze')}
    return totalMedals

# Returns the countries with the selected medal type in the selected sport
def countriesWithMedalInSport(sport, minMedal = 'Bronze'):
    with open('summer.csv', 'r', encoding = "utf8") as medalFile:
        medalInSport = csv.reader(medalFile)
        medalValues = {'Gold': 2, 'Silver': 1, 'Bronze': 0}
        countryCodes = []
        for line in medalInSport:
            if sport == line[2]:
                if medalValues[minMedal] <= medalValues[line[8]]:
                    countryCodes.append(line[5])
    with open('countries.csv', 'r', encoding = "utf8") as countriesFile:
        codeTranslate = csv.reader(countriesFile)
        next(codeTranslate)
        noDuplicate = []
        for country in codeTranslate:
            if country[1] not in countryCodes:
                noDuplicate.append(country[1])
    with open('countries.csv', 'r', encoding = "utf8") as countriesFile:
        codeTranslate = csv.reader(countriesFile)
        next(codeTranslate)
        countries = []
        for country in codeTranslate:
            if country[1] not in noDuplicate:
                countries.append(country[0])
        return countries

# Returns the number of gold medals won by the selected country in the selected year
def goldMedalsByCountryAndYears(code, minYear = 1896, maxYear = 2014):
    with open('summer.csv', 'r', encoding = "utf8") as medalInfo:
        goldCountries = csv.reader(medalInfo)
        next(goldCountries)
        athlete = []
        year = []
        discipline = []
        event = []
        gender = []
        for info in goldCountries:
            if code == info[5]:
                if info[8] == 'Gold':
                    if minYear <= int(info[0]) <= maxYear:
                        athlete.append(info[4])
                        year.append(info[0])
                        discipline.append(info[3])
                        event.append(info[7])
                        gender.append(info[6])
        return list(zip(athlete, year, discipline, event, gender))