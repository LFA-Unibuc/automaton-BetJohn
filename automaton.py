class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")

    def validate(self):
        """Return a Boolean

        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
        return "I can't tell if the config file is valid... yet!"

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        citire = open(input_str, "r")

        Alfabet = set()
        Stari = set()
        Tranzitii = []
        stari_finale = set()

        counter = 0
        text_input = citire.readlines()
        for linie in text_input:
            if linie.startswith('\n') or linie.startswith("#"):
                # inseamna ca trebuie sa ignor
                continue

            if "Sigma" in linie:
                # inseamna ca am intrat in alfabet
                counter = 1
                continue

            if 'States' in linie:
                # inseamna ca am intrat in stari
                continue

            if 'Transitions' in linie:
                # inseamna ca am intrat in tranzitii
                continue

            if linie.startswith('End'):
                # inseamna ca trec la urmatorul pas
                counter += 1
                continue

            if counter == 1:
                # pun in alfabet litera
                Alfabet.add(linie.strip())

            if counter == 2:
                if len(linie.strip().split(', ')) > 2:
                    Stari.add(linie.strip().split()[0])

                    if linie.strip().split(',')[2] == 'F':
                        stari_finale.add(linie.strip().split(' ,')[0])
                    if linei.strip().split(',')[2] == 'S':
                        initial_state = linei.strip().split(' ,')[0]
                    if linie.strip().split(',')[1] == 'F':
                        stari_finale.add(linie.strip().split(' ,')[0])
                    if linie.strip().split(',')[1] == 'S':
                        initial_state = linie.strip().split(' ,')[0]

                elif len(linie.strip().split(',')) == 2:
                    Stari.add(linie.strip().split()[0])
                    if linie.strip().split(',')[1] == 'S':
                        initial_state = linie.strip().split(' ,')[0]
                    if linie.strip().split(',')[1] == 'F':
                        stari_finale.add(linie.strip().split(' ,')[0])
                else:
                    Stari.add(linie.strip())
            if counter == 3:
                text = linie.strip().split(", ")
                for i in range(len(text)):
                    if i == 1:
                        text[i] = text[i][:-1]
                Tranzitii.append(tuple(text))
        este_ok = 1

        for tranzitie in Tranzitii:
            # aici verific ca toate elementele din tranzitii sa fie
            if tranzitie[0] not in Stari or tranzitie[2] not in Stari or tranzitie[1] not in Alfabet:
                print("Inputul nu este valid")
                este_ok = 0
        if este_ok == 1:
            print("Inputul este valid!")
        return 1


if __name__ == "__main__":
    a = Automaton('date.txt')
    a.read_input('date.txt')
