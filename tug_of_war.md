This is pseudocode.

start game
teamScore = 0
opponentScore = 0

function winGame():
    if teamScore == 10
        print("Success! Your team will move onto the next game.")
        restart game(Enter)
    elif opponentScore == 10
        print("Fail. You are eliminated. Enjoy your fall!")
        restart game(Enter)

function progressBar():
    if teamScore increases by one:
        move progress bar toward player
    elif opponentScore increases by one:
        move progress bar toward opponent

function opponentStrength():
    opponentStrength = random number 1-5
    set time based on opponentStrength
    
function gameplay():
    opponentStrength()
    while teamScore < 10 and opponentScore < 10:
        choose random arrow direction
        print("Arrow To Press:", chosenArrow)
        start opponent timer
        playerInput = get arrow from player
        if playerInput == chosenArrow:
            teamScore += 1
        else:
            teamScore -= 1
        winGame()
        
start gameplay()