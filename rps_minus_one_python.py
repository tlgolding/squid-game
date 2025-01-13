import random
import signal
import sys

def timeout_handler(signum, frame):
    print("\nTime's up! Fail.")
    play_rps_minus_one()
    your_score -= 1

def play_rps_minus_one():
    signal.signal(signal.SIGALRM, timeout_handler)
    rounds_played = 0
    your_score = 0
    
    while rounds_played < 6:
        options = ["rock", "paper", "scissors"]
        
        removed_option = random.choice(options)
        options.remove(removed_option)
        print(f"\nOne option is removed: {removed_option.upper()}")
        print(f"Choices left: {options}")
        
        signal.alarm(10)
        try:
            your_choice = input(f"Take back either {options[0]} or {options[1]}: ").lower()
            signal.alarm(0)  
        except TimeoutError:
            continue
        
        if your_choice not in options:
            print("Invalid. Let's play again.")
            play_rps_minus_one()
            return
        
        partner_choice = random.choice(options)
        print(f"partner chose: {partner_choice}")
        
        if your_choice == partner_choice:
            print("It's a tie!")
        elif (your_choice == "rock" and partner_choice == "scissors") or \
             (your_choice == "scissors" and partner_choice == "paper") or \
             (your_choice == "paper" and partner_choice == "rock"):
            print("Success!")
            your_score += 1
        else:
            print("Fail.")
        
        rounds_played += 1
        print(f"Score: {your_score} wins out of {rounds_played} rounds")
        
        # Check if the player wins the game
        if your_score >= 5:
            print("Success!")
            return
    
    # If the player didn't win 5 rounds
    print("You Lose. Play again?")
    play_rps_minus_one()

# Start the game
play_rps_minus_one()
