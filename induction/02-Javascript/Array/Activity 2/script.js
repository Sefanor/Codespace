let myArray = [20, 30, 25, 35, -16, 60, -100];

let sum = 0;

for (let i = 0; i < myArray.length; i++) {
    sum += myArray[i]
}

let average = sum/myArray.length;

alert(average)