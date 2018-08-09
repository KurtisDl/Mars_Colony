# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:52:32 2018

@author: Kurtis Dluge
"""
#import math
#if i get this all to work, use random chance of F or M at every birth
def colonyGrowth (StartingColonists: int, totalYears: int, startingAge: int,
                  birthStart: int, birthEnd: int, monthsBetweenBirths: int, deathAge: int) -> int:
    """Returns the number of subjects alive after a given time.
    Assumes 50% sex ratio, rounded down for female.
    Assumes 100% fertility sucsess.
    Assumes one offspring per pregnency.
    Uses inputs: startingColonists, startingAge(years), totalYears, monthsBetweenBirths, deathAge, birthStart, birthEnd, sexRatio"""
    
    Females = round(StartingColonists / 2)    
    startingAgeM = startingAge * 12
    deathAgeM = deathAge * 12
    totalYearsM = totalYears * 12
    birthStartM = birthStart * 12
    birthEndM = birthEnd * 12    
    totalMonthsPlusOne = totalYearsM + 1    
    monthsPassed = 0
    genAdd = 0
    topGen = 0
    totalCount = 0
    checkM = 0
    Generations = {}
    NotDead = {}
    NotDead[0] = {'total': 0, 'age': topGen}
    Generations[0] = {'total': StartingColonists, 'females': Females, 'age' : startingAgeM}
    if Generations[0]['age'] > birthStartM:
        checkM += 1
    while monthsPassed != totalMonthsPlusOne:
        if Generations[topGen]['age'] == birthEndM:
            NotDead[topGen] = {'total': Generations[topGen]['total'],
                               'age' : Generations[topGen]['age']}                    
            del Generations[topGen]
            topGen += 1                          
        oneMonthBirthCounter = 0
        for i in Generations:
            if Generations[i]['age'] > birthStartM and checkM == 1:
                oneMonthBirthCounter += Generations[i]['females']
                checkM = 0
            elif Generations[i]['age'] >= birthStartM and (Generations[i]['age'] - birthStartM) % monthsBetweenBirths == 0:
                oneMonthBirthCounter += Generations[i]['females']
        if oneMonthBirthCounter > 0:       
            genAdd += 1
            Generations[genAdd] = {'total': oneMonthBirthCounter,
                                   'females': int((oneMonthBirthCounter)/2),
                                   'age': 0}            
        if monthsPassed == totalYearsM:
            break        
        for i in Generations:
            Generations[i]['age'] += 1
        for i in NotDead:
            NotDead[i]['age'] += 1
        monthsPassed += 1
    for i in Generations:
        totalCount += Generations[i]['total']
    for i in NotDead:
        if NotDead[i]['age'] < deathAgeM:
            totalCount += NotDead[i]['total']
 
    return Generations, NotDead, totalCount

print (colonyGrowth(51, 10, 25, 16, 38, 13, 85))

#can use numpy.random.normal to get a normal distribution of the females at each birth set
#also, if i set the random seed with numpy.random.seed(put in number here), I will get the same result each time the program is run.
