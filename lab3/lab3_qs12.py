zodiacs = {
    2000 : "Dragon",
    2001 : "Snake",
    2002 : "Horse",
    2003 : "Sheep",
    2004 : "Monkey",
    2005 : "Rooster",
    2006 : "Dog",
    2007 : "Pig",
    2008 : "Rat",
    2009 : "Ox",
    2010 : "Tiger",
    2011 : "Hare"
}

year = int(input("Enter a year: "))
while year < 2000 :
    year = year + 12

for user_year in zodiacs :
    if year % user_year == 0 :
       