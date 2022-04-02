viz = []
pl = 1
linii = 0
matrix = []
Domeniu = []
Alfabet = set()
Stari = set()
Tranzitii = []
stari_finale = set()
ok = []
class Automaton():
    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")
    def validate(self, start):
        """Return a Boolean

        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
        global ok
        for x in Domeniu[4]:
            if str(x) == str(start):
                ok = 1
                return 
        viz[start-1] = 1
        for j in range(0,linii):
            if matrix[start-1][j] in Domeniu[1] and viz[j]==0:
                self.validate(j+1)
    
        if ok == 1:
            return "DFA Complete"
        else:
            return "I can`t tell if the config file is valid... yet!"

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        citire = open(input_str, "r")
        counter = 0
        Domeniu = []
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
                        stare_initiala = linei.strip().split(' ,')[0]
                    if linie.strip().split(',')[1] == 'F':
                        stari_finale.add(linie.strip().split(' ,')[0])
                    if linie.strip().split(',')[1] == 'S':
                        stare_initiala = linie.strip().split(' ,')[0]

                elif len(linie.strip().split(',')) == 2:
                    Stari.add(linie.strip().split()[0])
                    if linie.strip().split(',')[1] == 'S':
                        stare_initiala = linie.strip().split(' ,')[0]
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
                este_ok = 0
                return 0
        if este_ok == 1:
            # Voi face domeniul de definitii
            Domeniu.append(Stari)
            Domeniu.append(Alfabet)
            Domeniu.append(Tranzitii)
            Domeniu.append(stare_initiala)
            Domeniu.append(stari_finale)
            Domeniu = tuple(Domeniu)
            return Domeniu

if __name__ == "__main__":
    
    a = Automaton('date.txt')
    Domeniu = a.read_input('date.txt')
    if(a.read_input('date.txt')!=0):
        print("Inputul este valid!")
        linii = int(max(Domeniu[0]))
        matrix = []
        for i in range(linii):
            coloane = []
            for j in range(linii):
                coloane.append(0)
            matrix.append(coloane)
        tranzitii = Domeniu[2]
    # print(tranzitii)
        for i in range(linii):
            viz.append(0)
        for x in tranzitii:
            matrix[int(x[0])-1][int(x[2])-1] = x[1]
        ok = 0
        print(a.validate(int(Domeniu[3])))
    else:
        print("Inputul nu este valid")
    
# stari, alpfabet,tranzitii,stare intiala, stare finala

# int a[102][102],n,m,i,x,y,j,pl,coada[102],viz[102],u;
# int main()
# {
#     f>>n>>m>>pl;
#     for(i=1;i<=m;i++)
#     {
#         f>>x>>y;
#         a[x][y]=a[y][x]=1;
#     }
#     dfs(pl);
#     return 0;
# }