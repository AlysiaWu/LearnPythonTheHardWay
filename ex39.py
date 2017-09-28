# create a mapping of province to abbreviation
provinces = {
	'Jilin': 'jl',
	'Beijing': 'bj',
	'Shanxi': 'sx'
}

# create a basic set of states and some cities in them
cities = {
	'jl': 'Bai Shan',
	'bj': 'Hai Dian'
}

# add some more cities
cities['sx'] = 'Yan An'

print cities.get('sss')	#result: None
print cities.get('sx')	#result: Yan An
#print cities['sss']	#result: KeyError: 'sss'

# print out some cities
print '-' * 10
print "Shanxi Province has: ", cities['sx']
print "Jilin Province has: ", cities['jl']

# print some states
print '-' * 10
print "Jilin's abbreviation is: ", provinces['Jilin']
print "Beijing's abbreviation is: ", provinces['Beijing']

# do it by using the provinces then cities dict
print '-' * 10
print "Jilin has: ", cities[provinces['Jilin']]
print "Shanxi has: ", cities[provinces['Shanxi']]

# print every province abbreviation
print '-' * 10
for province, abbrev in provinces.items():
	print "%s is abbreviated %s" % (province, abbrev)
	
# print every city in province
print '-' * 10
for abbrev, city in cities.items():
	print "%s has city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for province, abbrev in provinces.items():
	print "%s province is abbreviated for %s and has city %s" % (
		province, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
province = provinces.get('Shandong', None)
if not province:
	print "Sorry, no Shandong."

# get a city with a default value
city = cities.get('sd', 'Does Not Exist')
print "The city for the province 'sd' is: %s" % city
