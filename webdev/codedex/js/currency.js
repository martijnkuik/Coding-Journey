let yuan = 560;
let yen =  2455;
let won = 3280;


console.log(yuan * 0.14 + yen * 0.0062 + won * 0.00072); // my first attempt, but I didnt like the 4 decimal places

// So I tried this approach
const totalUSD = yuan * 0.14 + yen * 0.0062 + won * 0.00072;
console.log(totalUSD.toFixed(2)); // This displays the result with 2 decimal places

