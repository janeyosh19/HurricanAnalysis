# names of hurricanes

from re import A


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

#Challeng #1 turn numbers with M in million and B with billion in float.

def updated_damages(damages):

    element_index = 0

    for damage in damages:
        if "M" in damage:
            damage_M = damage[:-1]
            damage_M = float(damage_M) *1000000
            damages[element_index] = damage_M
        if "B" in damage: 
            damage_B = damage[:-1]
            damage_B = float(damage_B) *1000000000
            damages[element_index] = damage_B

        element_index += 1

    return damages
        


updated_damage_list = updated_damages(damages)


#print(updated_damage_list)

# write your construct hurricane dictionary function here:

#make a key for name of hurricanes
#make a values Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death


def hurricane_dictionary(names, months, years, max_sustained_winds,areas_affected,damages,deaths):
    
    hurricane_names = names
    dictionary_hurricanes = {}

    hurricane_data = zip(names, months, years, max_sustained_winds,areas_affected,damages,deaths)
    hurricane_name_data = zip(hurricane_names, hurricane_data)
    dictionary_hurricanes = dict(hurricane_name_data)

    return dictionary_hurricanes

dictionay_2_hurricanes = hurricane_dictionary(names, months, years, max_sustained_winds,areas_affected,damages,deaths)

#print(dictionay_2_hurricanes)

# write your construct hurricane by year dictionary function here: #4 it has a zip object when you print it

def year_hurricane_dictionary(years, hurricane_data):
    
    Year_as_key = {key: value for key, value in zip(years, hurricane_data)}
    return Year_as_key


year_hurricane_data = year_hurricane_dictionary(years, hurricane_dictionary(names, months, years, max_sustained_winds,areas_affected,damages,deaths))

#print(year_hurricane_data)

# write your count affected areas function here: # problem with especially, # uppercase problem


area_affect_title = [] #using title()
for areas in areas_affected:
    for area in areas:
        area_affect_title.append(area.title())


print(area_affect_title)


def affected_area_count(area_affect_title):
  
    affected_area_list_numbers = {}

    
    affected_area_list_numbers = dict((area, area_affect_title.count(area)) for area in area_affect_title)

    return affected_area_list_numbers


affected_area_counting_list = affected_area_count(area_affect_title)

print(affected_area_counting_list)

# write your find most affected area function here:

def most_affected_area(affected_area_counting_list):
    
    area_values = affected_area_counting_list.values()
    area_values_list = []
    most_affected = None
    for area_value in area_values:
            area_values_list.append(area_value)
            most_affected = max(area_values_list)
    for area, affected_times in affected_area_counting_list.items():
            if affected_times == most_affected:
                return area, affected_times

    
affected_area_the_most = most_affected_area(affected_area_counting_list)

#print(affected_area_the_most)


# write your greatest number of deaths function here: 

dictionary_Name_death = {key: value for key, value in zip(names, deaths)}

def greatest_deaths(dictionary_Name_death):

    deaths_list = []
    max_death = None
    for death in dictionary_Name_death.values():
            deaths_list.append(death)
            max_death = max(deaths_list)
    for name, death in dictionary_Name_death.items():
            if death == max_death:
                return name, death
    
        
greatest_hurricane_deaths = greatest_deaths(dictionary_Name_death)

#print(greatest_hurricane_deaths)

# write your categorize by mortality function here:


def mortality_rates(deaths):

    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    
    
    for death in deaths:
        if death in range(0,99):
            hurricanes_by_mortality[0].append(death)
        elif death in range(100, 499):
            hurricanes_by_mortality[1].append(death)
        elif death in range(500, 999):
            hurricanes_by_mortality[2].append(death)
        elif death in range(1000, 9999):
            hurricanes_by_mortality[3].append(death)
        elif death in range(10000, ):
            hurricanes_by_mortality[4].append(death)
    return hurricanes_by_mortality

#print(mortality_rates(deaths))


# write your greatest damage function here:

Names_and_damages = {key: value for key, value in zip(names, updated_damage_list)}

def greatest_damage(Names_and_damages):

    values = Names_and_damages.values()
    values_list = []
    value_list_max = None
    for value in values:
        value_float = isinstance(value, float)
        if value_float == True:
            value_integer = int(value)
            values_list.append(value_integer)
            value_list_max = max(values_list)
    for name, damages in Names_and_damages.items():
        if damages == value_list_max:
            return name, damages 
            
       
greates_damage_cost = greatest_damage(Names_and_damages)

#print(greates_damage_cost)

# write your categorize by damage function here: #return 

def damage_scale(updated_damage_list):

    damage_int = []
    for damages in updated_damage_list:
        damages_float = isinstance(damages, float)
        if damages_float == True:
            damages_int = int(damages)
            damage_int.append(damages_int)
    
    
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    
    
    for damage in damage_int:
        if damage in range(0,99999999):
            hurricanes_by_damage[0].append(damage)
        elif damage in range(100000000, 999999999):
            hurricanes_by_damage[1].append(damage)
        elif damage in range(1000000000, 9999999999):
            hurricanes_by_damage[2].append(damage)
        elif damage in range(10000000000, 99999999999):
            hurricanes_by_damage[3].append(damage)
        elif damage in range(50000000000, 50000000000):
            hurricanes_by_damage[4].append(damage)
        elif damage in range(50000000001, ):
            hurricanes_by_damage[5].append(damage)

    return(hurricanes_by_damage)
        

hurricanes_damage_scale = damage_scale(updated_damage_list)
#print(hurricanes_damage_scale)

