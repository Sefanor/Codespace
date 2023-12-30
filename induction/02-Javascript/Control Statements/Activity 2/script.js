let a = prompt("Input first number:");
let b = prompt("Input second number:");
let c = prompt("Input third number:");

if (a < b && b < c) {
    alert("Increasing order");
} else if (a > b && b > c) {
    alert("Decreasing order");
} else {
    alert("Not increasing nor decreasing order");
}
