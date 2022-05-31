from datetime import date
#import datetime
names=["imposter","sussybka","crewmate","aMoNgUs","CaMpEr"]
years = [1989,1985,1996,2006,2018]
current_date = date.today()
current_year = current_date.year
print(current_year)
ages = [current_year - year for year in years]
print(ages)