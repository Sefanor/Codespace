let myArray = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49];

let min = max = myArray[0];

for (let i = 0; i < myArray.length; i++) {
    if (myArray[i] < min) {
        min = myArray[i]
    }
    if (myArray[i] > max) {
        max = myArray[i]
    }
}

alert("Min: is " + min);
alert("Max: is " + max);