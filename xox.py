import turtle

# Set up the screen and the window name
screen = turtle.Screen()
screen.title("Turtle XOX Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create turtles
drawer = turtle.Turtle()
drawer.speed(10)  # Maximum speed for drawing
drawer.pensize(3)
drawer.hideturtle()

player_turtle = turtle.Turtle()
player_turtle.speed(10)  # Maximum speed for drawing
player_turtle.pensize(5)
player_turtle.hideturtle()

message_turtle = turtle.Turtle()
message_turtle.hideturtle()

# We initialize game variables
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

#Our flags and counters 
current_player = "X"
game_over = False
rounds_played = 0
player_x_score = 0
player_o_score = 0
move_counter = 0
move_in_progress = False

#Draw the grid
def draw_grid():
    clear_message() 
    drawer.clear()
    drawer.penup()
    for i in range(2):
        drawer.goto(-300 + 200 * (i + 1), -300)
        drawer.pendown()
        drawer.goto(-300 + 200 * (i + 1), 300)
        drawer.penup()
    for i in range(2):
        drawer.goto(-300, -300 + 200 * (i + 1))
        drawer.pendown()
        drawer.goto(300, -300 + 200 * (i + 1))
        drawer.penup()

# Draw X
def draw_x(x, y):
    clear_message() 
    global move_in_progress
    move_in_progress = True
    
    player_turtle.color("black")
    player_turtle.penup()
    player_turtle.goto(x - 60, y + 60)
    player_turtle.pendown()
    player_turtle.goto(x + 60, y - 60)
    player_turtle.penup()
    player_turtle.goto(x + 60, y + 60)
    player_turtle.pendown()
    player_turtle.goto(x - 60, y - 60)
    player_turtle.penup()
    
    move_in_progress = False

# Draw O
def draw_o(x, y):
    clear_message() 
    global move_in_progress
    move_in_progress = True

    player_turtle.color("black")
    player_turtle.penup()
    player_turtle.goto(x, y - 60)
    player_turtle.pendown()
    player_turtle.circle(60)
    player_turtle.penup()
    
    move_in_progress = False

# Check for a win
def check_win(player):
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

# Check if the board is full so we understand the if it is a tie or not 
def is_board_full():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

# Display a message with a background covered
def display_message_with_bg(message, bg_color):
    message_turtle.clear()  
    
    message_turtle.penup()
    message_turtle.goto(-150, 0)
    message_turtle.pendown()
    message_turtle.color(bg_color)
    message_turtle.begin_fill()
    message_turtle.goto(150, 0)
    message_turtle.goto(150, -30)
    message_turtle.goto(-150, -30)
    message_turtle.goto(-150, 0)
    message_turtle.end_fill()
    message_turtle.penup()
    
    message_turtle.color("black")
    message_turtle.goto(0, -20)
    message_turtle.write(message, align="center", font=("Arial", 12, "bold"))

def clear_message():
    message_turtle.clear()



def click_handler(x, y):
    global current_player, game_over, rounds_played, player_x_score, player_o_score, move_counter

    if game_over or move_in_progress:
        return

    if move_counter >= 9:
        return

    col = int((x + 300) // 200)
    row = int((y + 300) // 200)

    if row >= 0 and row < 3 and col >= 0 and col < 3:
        if board[row][col] == "":
            board[row][col] = current_player
            x_pos = col * 200 - 300 + 100
            y_pos = row * 200 - 300 + 100

            if current_player == "X":
                draw_x(x_pos, y_pos)
            else:
                draw_o(x_pos, y_pos)

            move_counter += 1

            if check_win(current_player):
                if current_player == "X":
                    player_x_score += 1
                else:
                    player_o_score += 1

                display_message_with_bg(f"Player {current_player} wins!", "lightgreen")
                game_over = True
                rounds_played += 1
                screen.ontimer(show_restart_screen, 3000)
            else:
                if is_board_full() or move_counter >= 9:
                    display_message_with_bg("It's a tie!", "lightblue")
                    game_over = True
                    rounds_played += 1
                    screen.ontimer(show_restart_screen, 3000)
                else:
                    current_player = "O" if current_player == "X" else "X"

def restart_game_from_space():
    global rounds_played, player_x_score, player_o_score, game_over, move_counter, board
    rounds_played = 0
    player_x_score = 0
    player_o_score = 0
    game_over = False
    move_counter = 0
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    player_turtle.clear()
    screen.bgcolor("white")
    start_game()

def show_restart_screen():
    player_turtle.clear()
    drawer.clear()
    display_message_with_bg("Game Over! Press Space to restart.", "lightgreen")
    screen.onkey(restart_game_from_space, "space")

# Introduction screen
def introduction():
    display_message_with_bg("Welcome to Turtle XOX Game! Press Space to start.", "lightblue")
    screen.onkey(start_game, "space")

# Start the game
def start_game():
    global game_over
    if game_over:
        return
    player_turtle.clear()
    draw_grid()
    screen.onclick(click_handler)
    screen.onkey(None, "space")  

# Main
introduction()
screen.listen()
screen.mainloop()
