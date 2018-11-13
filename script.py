destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'So Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', 'historical site', 'art']

def get_destination_index(destination):
  destination_index = destination.index(1,2,3,4,5)
  return destination_index
get_destination_index("Los Angeles, USA")