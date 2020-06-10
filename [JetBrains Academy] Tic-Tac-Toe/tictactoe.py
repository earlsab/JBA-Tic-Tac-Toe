def board():
    print(f"""---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------""")


def process(cp):
    global check
    check = 0
    cp = cp.split()
    try:
        cp = [int(i) for i in cp]
        cp = [i for i in cp if (i > 0) and (i < 4)]
        check += 1
        if len(cp) == 2:
            check += 1
        else:
            print("Coordinates should be from 1 to 3!")
    except ValueError:
        print("You should enter numbers!")

    for x in range(len(num_list)):
        if cp == num_list[x]:
            if cells[x] == " ":
                check += 1
                break
            else:
                print("This cell is occupied! Choose another one!")
    return cp


def coordinates(xy):
    global cells, move_counter, num_list
    num_list = [[1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]
    tc = process(xy)
    if check == 3:
        for x in range(len(num_list)):
            if tc == num_list[x]:
                move_counter += 1
                if move_counter % 2 == 0:
                    cells[x] = "O"
                    break
                else:
                    cells[x] = "X"
                    break


def game_state():
    global game
    horizontal = [[cells[x], cells[x + 1], cells[x + 2]] for x in range(0, 7, 3)]
    vertical = [[cells[x], cells[x + 3], cells[x + 6]] for x in range(3)]
    diagonal = [[cells[x], cells[4], cells[x + 2]] for x in [0, 6]]
    list_cells = [horizontal, vertical, diagonal]
    blank = len(list(b for b in cells if b == " "))
    win_count = 0
    win_player = []

    for direction in list_cells:  # checks if there are any lines "won"
        for line in direction:
            if all(x == line[0] for x in line) and (line[0] != " "):  # checks if a list has all the same elements
                win_count += 1
                win_player = line[0]
                break

    if (win_count == 0) and (blank > 0):
        pass
    elif (win_count == 0) and (blank == 0):
        print("Draw")
        game = 0
    elif win_count == 1:
        print(f"{win_player} wins")
        game = 0


game = True
cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
move_counter = 0
while game:
    coordinates(input("Enter the coordinates: "))
    board()
    game_state()
