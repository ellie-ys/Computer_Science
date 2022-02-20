const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (
    userInput === "rock" ||
    userInput === "paper" ||
    userInput === "scissors"
  ) {
    return userInput;
  } else {
    console.log("Error!");
  }
};

// console.log(getUserChoice('Rock'));
// console.log(getUserChoice('Scissors'));

const getComputerChoice = () => {
  let userInt = Math.floor(Math.random() * 3);
  switch (userInt) {
    case 0:
      userInput = "rock";
      break;
    case 1:
      userInput = "paper";
      break;
    case 2:
      userInput = "scissors";
      break;
  }
  return userInput;
};
// console.log(getComputerChoice());
// console.log(getComputerChoice());
// console.log(getComputerChoice());
const userChoice = getUserChoice("scissors");
const computerChoice = getComputerChoice();

const determineWinner = (userChoice, computerChoice) => {
  if (userChoice === computerChoice) {
    return "The game is a tie!";
  } else {
    if (userChoice === "rock") {
      if (computerChoice === "paper") {
        return "The winner is Computer!";
      } else {
        return "The winner is User";
      }
    }
    if (userChoice === "paper") {
      if (computerChoice === "scissors") {
        return "computer is won!";
      } else {
        return "user is won";
      }
    }

    if (userChoice === "scissors") {
      if (computerChoice === "rock") {
        return "the computer is won!";
      } else {
        //computer choice is paper
        return "user is won!";
      }
    }
  }
};
