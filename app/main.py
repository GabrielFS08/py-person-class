class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for peo in people:
        Person(peo["name"], peo["age"])
    for peo in people:
        person_inst = Person.people[peo["name"]]
        wife_name = peo.get("wife")
        if wife_name:
            person_inst.wife = Person.people[wife_name]
        husband_name = peo.get("husband")
        if husband_name:
            person_inst.husband = Person.people[husband_name]
    return [Person.people[peo["name"]] for peo in people]
