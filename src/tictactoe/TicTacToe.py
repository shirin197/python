"""
@Nadina Shirin Amsler (shirin197)
@2021-05-03
@tictactoe

Spielfeld
   | 0 |

X  | X | X

   |  |
"""
"""
Gelernte/repetierte statment etc.
pass : Platzhalter für zukünftigen Code, so vermeiden wir, dass wir einen Fehler erhalten, wenn leerer Code nicht erlaubt ist
constructor : baut uns alles
self : repräsentiert die Instanz der Klasse
       kann auf Attribute und Methoden der Klasse zugreifen
elif : if...elif..else 
def : Schlüsselwort für eine Funktion
"""

class Board:

    def __init__(self): # Constructor
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def make_turn(self, cell, player): # Argumente (args)
         if self.is_valid_turn(cell):
             # self enthält sein eigenes attribut
            self.state[cell] = player.symbol
            return True
         return False

    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

# Gewinn Möglichkeiten die wir produzieren können //7 Wie man das Spiel gewinnen kann
    def check_win(self, player):
        s = player.symbol # Überprüft ob es funktionier (nur für ein Spieler)
        # Wertikale WINS
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True
        # Horizontale WINS
        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True
        # Diagonale WINS
        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def is_full(self):
        for i in self.state:
            if i == 0: # nicht voll ->
                return False # Ausgabe False sonst true
            return True

    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"

    def print_board(self):
        print(" " + self.sign_to_printable(self.state[0]) + " | " + self.sign_to_printable(self.state[1]) + "  | " + self.sign_to_printable(self.state[2]) + "  \n" +
              " " + self.sign_to_printable(self.state[3]) + " | " + self.sign_to_printable(self.state[4]) + "  | " + self.sign_to_printable(self.state[5]) + "  \n" +
              " " + self.sign_to_printable(self.state[6]) + " | " + self.sign_to_printable(self.state[7]) + "  | " + self.sign_to_printable(self.state[8]) + "  \n")
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

if __name__ == '__main__':
    player_a = Player(1)
    player_b = Player(2)
    board = Board()
    active_player = player_a # Player a ist der aktive spieler
    while not board.is_full(): # Solange das board nicht voll ist lassen wir es laufen // sonst ein break (Z. 105)
        board.print_board() # Board wird ausgegeben
        try:
             # die Eingabe muss in eine integer umgewandelt werden, weil wir eine Zahl von 0-8 enpfangen müssen
             cell = int(input("Wo möchtest du dein Zeichen platzieren? [1-9]"))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8: # Wenn die Eingabe nicht dem Entsprich gibt es einfach die *Frage* nochmals aus
            print("Bitte gebe eine Nummer zwischen 1 und 9 ein") # *Frage*
            continue
        if not board.make_turn(cell, active_player): # Wenn nicht
            print("Ungültiger Zug")
            continue
        if board.check_win(active_player):
            print("Du hast gewonnen!")
            break

        if active_player == player_a:
            active_player = player_b
        else:
            active_player = player_a
    print("Es war ein Versuch")






