class DogBreed:
    species = 'canis familiaris'  

    def __init__(self, name, origin):
        self.name = name           
        self.origin = origin       

    def display_details(self):
        print("Breed Name: " + self.name)
        print("Origin: " + self.origin)
        print("Species: " + DogBreed.species)


dog1 = DogBreed('golden retriever', 'scotland')
dog2 = DogBreed('shiba inu', 'japan')

dog1.display_details()
print()
dog2.display_details()
