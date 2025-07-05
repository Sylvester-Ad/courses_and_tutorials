document.addEventListener("DOMContentLoaded", () => {

    // Define object to track scores
    const score = JSON.parse(localStorage.getItem("score")) || {
        wins: 0,
        losses: 0,
        ties: 0
    };
    updateScoreElement();



    // Define function to pick computer's guess
    function pickComputerGuess() {
        let computerGuess = "";

        // Randomly assign value(rock, paper, scissors) to computer
        const randomNumber = Math.floor(Math.random() * 3);
        console.log(randomNumber);
        if (randomNumber === 0) {
            computerGuess = "rock";
        }
        else if (randomNumber === 1) {
            computerGuess = "paper";
        }
        else {
            computerGuess = "scissors";
        }
        return computerGuess;
    }

    function letComputerThink(callback) {
        // Hide results
        document.getElementById("results-area").classList.add("hidden");

        // Show spinner and thinking text
        document.getElementById("thinking-area").classList.remove("hidden");

        // Wait for 1 second before running callback (actual game logic)
        setTimeout(() => {
            document.getElementById("thinking-area").classList.add("hidden");
            callback(); // continue with game
        }, 1000);
    }


    // Define game function
    function playGame(userGuess) {
        letComputerThink(() => {
            const computerGuess = pickComputerGuess();


            let result;
            const resultEl = document.getElementById("result");

            // Assign result based on choice
            if (userGuess === computerGuess) {
                result = "Tie!";

                // Update score
                score.ties += 1;
                resultEl.classList = ("result-tie fadeIn");
            }
            else if (
                (userGuess === "rock" && computerGuess === "paper") ||
                (userGuess === "paper" && computerGuess === "scissors") ||
                (userGuess === "scissors" && computerGuess === "rock")
            ) {
                result = `You lose. Computer chose ${computerGuess}`;

                // Update score
                score.losses += 1;
                resultEl.classList = "result-lose fadeIn";
            } else {
                result = `You win! Computer chose ${computerGuess}`;

                // Update score
                score.wins += 1;
                resultEl.classList = "result-win fadeIn";
            }

            // Store score in localStorage
            localStorage.setItem("score", JSON.stringify(score));

            // Update score element
            updateScoreElement();

            // Show result
            resultEl.innerHTML = `<p>${result}</p>`;
            document.getElementById("results-area").classList.remove("hidden");
            

            // Show moves
            document.getElementById("moves").innerHTML =
                `<p class="fadeIn">
                    You
                    <img class="move-icon" src="images/${userGuess}-emoji.svg">
                    <img class="move-icon" src="images/${computerGuess}-emoji.jpg">
                    Computer
                </p>`;
        })
    }

    // Select all game buttons
    const buttons = document.querySelectorAll(".game");

    // Play game when button is clicked
    buttons.forEach(btn => {
        btn.addEventListener("click", () => playGame(btn.value));
    });

    // Reset score upon clicking reset score button
    const resetScoreButton = document.getElementById("reset-score");
    resetScoreButton.onclick = () => {
        // Reset all scores
        score.losses = 0;
        score.wins = 0;
        score.ties = 0;

        // Update score in UI
        updateScoreElement();

        // Remove item from localStorage
        localStorage.removeItem("score");
    };

    function updateScoreElement() {
        // Display scores
        document.getElementById("scores").innerHTML =
            `<p>Wins: ${score.wins}, Losses: ${score.losses}, Ties: ${score.ties}</p>`;
    }
})