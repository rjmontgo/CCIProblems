from problem_6 import AnimalShelter


def test_all_dogs():
    animalShelter = AnimalShelter()
    animalShelter.addDog()
    animalShelter.addDog()
    animalShelter.addDog()

    assert 0 == animalShelter.removeDog()
    assert 1 == animalShelter.removeEither()
    assert 2 == animalShelter.removeDog()

def test_all_cats():
    animalShelter = AnimalShelter()
    animalShelter.addCat()
    animalShelter.addCat()
    animalShelter.addCat()

    assert 0 == animalShelter.removeCat()
    assert 1 == animalShelter.removeEither()
    assert 2 == animalShelter.removeCat()

def test_mix_dogs_and_cats():
    animalShelter = AnimalShelter()
    animalShelter.addCat()
    animalShelter.addDog()
    animalShelter.addCat()
    animalShelter.addCat()
    animalShelter.addCat()

    assert 0 == animalShelter.removeCat()
    assert 1 == animalShelter.removeEither()
    assert 2 == animalShelter.removeCat()
