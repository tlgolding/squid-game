let yourMarbles = 10;
let gganbuMarbles = 10;


// when you have either lost or won
function endGame() {
	if (yourMarbles == 0) {
		alert("Sorry, you have been eliminated");
	} else if (yourMarbles >= 20) {
		alert("Congratulations, you have won the game.");
	}
	return;
}

// if you're wrong your wager goes to your gganbu
function yourTurn() {
	// make a bet from 1-5 marbles
	const wager = parseInt(prompt("You may bet up to five marbles."), 10);
	if (wager < 1 || wager > 5 || wager > yourMarbles) {
		console.log("Invalid wager. Try again.");
		return yourTurn();
	}

	const gChoice = Math.floor(Math.random() * 5) + 1;
	const guess = prompt("Did they choose an even or odd number?");
	const isEven = gChoice % 2 === 0;

	if ((guess === "even" && isEven) || (guess === "odd" && !isEven)) {
		console.log("Pass. You win their choice.");
		yourMarbles += gChoice;
		gganbuMarbles -= gChoice;
	} else {
		console.log("Fail. They win your wager.");
		yourMarbles -= wager;
		gganbuMarbles += wager;
	}

	endGame();
	return;
}

function gganbuTurn() {
	const choice = parseInt(prompt("Choose up to five marbles to hide"), 10);
	if (choice < 1 || choice > 5 || choice > yourMarbles) {
		console.log("Invalid choice. Try again.");
		return gganbuTurn();
	}

	const gWager = Math.floor(Math.random() * 5) + 1;
	const gChoice = Math.random() < 0.5 ? "even" : "odd";
	const isEven = choice % 2 === 0;

	console.log("It is now your Gganbu's choice to guess.");
	console.log(`They guessed ${gChoice}.`)
	if ((gChoice === "even" && isEven || gChoice === "odd" && !isEven)) {
		console.log("Fail. You lose your choice.");
		yourMarbles -= choice;
		gganbuMarbles += choice
	} else {
		console.log("Pass. You win their wager.");
		yourMarbles += gWager;
		gganbuMarbles -= gWager;
	}

	endGame();
	return;
}