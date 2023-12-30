let output  = document.querySelector(".container-output");

let containerBtn  = document.querySelector(".container-btn");

const randomChoice = () => {
    let n =  Math.floor(Math.random() * 3);
    switch (n) {
        case 0:
            return "Rock";
        case 1:
            return "Paper";
        case 2:
            return "Scissors";
    }
}

let play = function(choice) {
    let computerChoice = randomChoice().toLowerCase();

    let result;

    if (choice.toLowerCase() === computerChoice) {
        result = 0;
    }

    if (choice.toLowerCase() === "rock" && computerChoice === "scissors") {
        result = 1;
    }

    if (choice.toLowerCase() === "rock" && computerChoice === "paper") {
        result = -1;
    }

    if (choice.toLowerCase() === "paper" && computerChoice === "rock") {
        result = 1;
    }

    if (choice.toLowerCase() === "paper" && computerChoice === "scissors") {
        result = -1;
    }

    if (choice.toLowerCase() === "scissors" && computerChoice === "paper") {
        result = 1;
    }

    if (choice.toLowerCase() === "scissors" && computerChoice === "rock") {
        result = -1;
    }
    
    let yourChoice = document.createElement("div");
    yourChoice.textContent = "Your choice: " + choice;

    let itsChoice = document.createElement("div");
    itsChoice.textContent = "Computer choice: " + computerChoice;

    let resultText = document.createElement("div");
    resultText.textContent = "Result: ";
    
    if (result === 1) {
        resultText.textContent += "You win!";
    }
    if (result === 0) {
        resultText.textContent += "Draw!";
    }
    if (result === -1) {
        resultText.textContent += "You Lose!";
    }

    output.innerHTML = "";

    output.appendChild(yourChoice);
    output.appendChild(itsChoice);
    output.appendChild(resultText);
}

containerBtn.addEventListener("click", (event) => {
    play(event.target.textContent.toLowerCase())
})