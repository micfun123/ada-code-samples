# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_oop_concepts

from pet_class import Pet

def main():
    pet_name = input("Enter the name of your pet ")
    pet_type = input(f"What type of animal is {pet_name}? ")
    pet_colour = input(f"What colour is {pet_name}? ")
    my_pet = Pet(pet_name, pet_type, pet_colour)  # Instantiation
    print(my_pet)  # Will show that a pet object has been created
   
if __name__ == "__main__":
    main()
