# python code that includes:
# inputs, operators, functions, if statements, while loops, booleans, opening files, and web scraping
#------------------------------------------------------------------------------

# basic paycheck calculator with overtime factored in
hrs=input('Enter Hours:')
rate=input('Enter Rate:')
fhrs=float(hrs)
frate=float(rate)
if fhrs<=40:
    regpay=fhrs*frate
    otpay=0
else:
    regpay=40*frate
    otpay=(fhrs-40)*(frate*1.5)
def computepay():
    return regpay+otpay
print('Pay:',computepay())
#----------------------------------------------------------------------------

# searches through the user-provided file name (text file),
# finds the line that includes searched text and locates the integer on that line,
# calculates the average of all of the integers
fname = input('Enter the file name: ')
if fname == 'OLD FILE':
    print("This is an old file.  DO NOT USE!")
    quit()
try:
    fhand = open(fname)
except:
    print(fname,'is a bad file name')
    quit()
count = 0
summ = 0
find_txt = 'X-DSPAM-Confidence:'
for ea_line in fhand:
    if ea_line.startswith(find_txt):
        count = count+1
        num_start=find_txt.find(':')
        num=ea_line[num_start+1:]
        num=float(num)
        summ=summ+num
avg=summ/count
print('AVG spam confidence:',avg)
#------------------------------------------------------------------------------

# functions to calculate circumferece and diameter of a circle using object oriented programming
class Circle():
    pi=3.14444

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi #JS self.pi would work here also

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius **2 * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2

    def diameter(self):
        return self.radius*2
#------------------------------------------------------------------------------

#tic tac toe game using python functions, while loops, if statements, booleans

from IPython.display import clear_output

# create board
def display_board(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('   |   |   ')
# function to make sure players are inputting x or o
def player_input():
    mark = ''
    while mark != 'X' and mark != 'O':
        mark = input('Player 1: Would you like to be X or O?   ').upper()
    if mark == 'X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board, marker, position):
    board[position]=marker
# function to check if anyone has won (column-win not completed)
def win_check(board, mark):
    return((mark==board[1]==board[2]==board[3]) or
    (mark==board[4]==board[5]==board[6]) or
    (mark==board[7]==board[8]==board[9]) or
    (mark==board[1]==board[5]==board[9]) or
    (mark==board[3]==board[5]==board[7]))

import random
# function to randomly choose who goes first
def choose_first():
    if random.randint(1,2)==1:
        print('The powers-that-be have decided that Player 1 goes first!')
        return (1,2)
    else:
        print('The powers-that-be have decided that Player 2 goes first!')
        return (2,1)

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' in board
#function to see if spot is taken
def player_choice(board):
    position = 0

    while int(position) not in range(1,10):
        position = input ('Please choose your position (1-9):   ')
    while space_check(board,int(position)) == False:
            position = input ('That spot is taken. Please choose another position (1-9):   ')
    position=int(position)
    return position
#function to play again
def replay():
    playagn = ' '
    while playagn != 'Yes' and playagn != 'No':
        playagn = input('Would you like to play again? (Yes or No)')
    if playagn == 'Yes':
        return True
    else:
        return False
# the key to show the position number of each box
boardkey = ['#','1','2','3','4','5','6','7','8','9']
# function to play the game
def play_tictactoe():
    print('Welcome to Tic Tac Toe!')
    print(' ')
    print('Below are the position numbers for choosing where to put your mark.')
    print(' ')
    print("When it's your turn, you must enter a number from 1 to 9.")
    print(' ')
    display_board(boardkey)
    print(' ')
# players choose x or o, and than computer chooses who goes first
    (player1_marker,player2_marker) = player_input()
    print(' ')
    (first_player, second_player) = choose_first()
    print(' ')
    print(' ')

    if first_player == 1:
        first_player_marker = player1_marker
        second_player_marker = player2_marker
    else:
        first_player_marker = player2_marker
        second_player_marker = player1_marker

    newboard = [' ']*10
    newboard[0]='#'

    while full_board_check(newboard) == False:
    # first player turn
        print(f'Player {first_player}')
        nextspot = player_choice(newboard)
        print(nextspot)
        newboard[nextspot]=first_player_marker
        clear_output()
        display_board(newboard)
        print('')

        if win_check(newboard,first_player_marker) == True:
            print(f'PLAYER {first_player} WINS!')
            play_choice = replay()
            if play_choice == True:
                play_tictactoe()
            else:
                print('Thanks for playing!')
                exit()
        elif full_board_check(newboard) == False:
     # second player turn
            print(f'Player {second_player}')
            nextspot = player_choice(newboard)
            newboard[nextspot]=second_player_marker
            clear_output() # used to clear the views of previous turns
            display_board(newboard)
            print('')
            if win_check(newboard,second_player_marker) == True:
                print(f'PLAYER {second_player} WINS!')
                play_choice = replay()
                if play_choice == True:
                    play_tictactoe()
                else:
                    print('Thanks for playing!')
                    exit()
            elif full_board_check(newboard) == True:
                print("Cat's Game!  It's a tie.")
                play_choice = replay()
                if play_choice == True:
                    play_tictactoe()
                else:
                    print('Thanks for playing!')
                    exit()
        elif full_board_check(newboard) == True:
            print("Cat's Game!  It's a tie.")
            play_choice = replay()
            if play_choice == True:
                play_tictactoe()
            else:
                print('Thanks for playing!')
                exit()
#------------------------------------------------------------------------------

# scrapes the bookstoscrape.com website and creates list of all titles with a two star rating

import requests
import bs4
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

two_star_titles = []
count = 0

for ea_pg in range(1,51): #we know there are 50 pages of book titles
    scrape_url = base_url.format(ea_pg)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')

    for ea_book in books:
        if len(ea_book.select('.star-rating.Two')) != 0:
            book_title = ea_book.select('a')[1]['title']
            count += 1
            two_star_titles.append(str(count)+'. '+book_title+' pg.'+str(ea_pg))
