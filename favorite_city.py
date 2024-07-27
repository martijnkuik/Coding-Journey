class City:   
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

    def __str__(self):
        return f'City: {self.name}, Country: {self.country}, Population: {self.population}, Landmarks: {self.landmarks}'

my_city = City('Meppel', 'The Netherlands', '35.814', 'Wilhelminapark')

print(my_city)