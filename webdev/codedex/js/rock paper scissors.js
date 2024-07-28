/* Rock wins against scissors but loses against paper
Scissors wins against paper but loses against rock
Paper wins against rock but loses against scissors */



let choices = ["rock", "paper", "scissors"];
let player = choices[Math.floor(Math.random() * 3)];
let computer = choices[Math.floor(Math.random() * 3)];

console.log("Player picked:", player);
console.log("Computer picked:", computer);

// Determine winner based on player choice
if (player === "rock") {
  if (computer === "scissors") {
    console.log("Player wins!");
  } else {
    console.log("Computer wins!");
  }
} else if (player === "paper") {
  if (computer === "rock") {
    console.log("Player wins!");
  } else {
    console.log("Computer wins!");
  }
} else if (player === "scissors") {
  if (computer === "paper") {  
    console.log("Player wins!");
  } else {
    console.log("Computer wins!");
  }
} else {
  console.log("Something went wrong!"); 
}
