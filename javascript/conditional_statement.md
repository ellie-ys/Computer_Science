# If Statement

```
let sale = true;

sale = false;
if(sale == true){console.log('Time to buy!')};
```

# If...Else Statements

```
let sale = true;

sale = false;

if(sale) {
  console.log('Time to buy!');
} else {
  console.log('Time to wait for a sale.');
}
```

# Comparison Operators

Less than: <  
Greater than: >  
Less than or equal to: <=  
Greater than or equal to: >=  
Is equal to: ===  
Is not equal to: !==

```
let hungerLevel = 7;

if (hungerLevel>7) {
  console.log('Time to eat!');

}else{
  console.log('We can eat later!');
}
```

# Logical Operators

There are three logical operators:

the and operator (&&)  
the or operator (||)  
the not operator, otherwise known as the bang operator (!)

```
//When we use the && operator, we are checking that two things are true:
if (stopLight === 'green' && pedestrians === 0) {
  console.log('Go!');
} else {
  console.log('Stop');
}
```

```
//If we only care about either condition being true, we can use the || operator:
if (day === 'Saturday' || day === 'Sunday') {
  console.log('Enjoy the weekend!');
} else {
  console.log('Do some work.');
}
```

```
//The ! not operator reverses, or negates, the value of a boolean:
let excited = true;
console.log(!excited); // Prints false

let sleepy = false;
console.log(!sleepy); // Prints true
```

```
let mood = 'sleepy';
let tirednessLevel = 6;


if(mood==='sleepy' && tirednessLevel > 8){
  console.log('time to sleep');
}else{
  console.log('not bed time yet');
}
```

# Truthy and Falsy

So which values are falsy— or evaluate to false when checked as a condition? The list of falsy values includes:

0  
Empty strings like "" or ''  
null which represent when there is no value at all  
undefined which represent when a declared variable lacks a value  
NaN, or Not a Number

```
//example
let numberOfApples = 0;

if (numberOfApples){
   console.log('Let us eat apples!');
} else {
   console.log('No apples left!');
}

// Prints 'No apples left!'
```

```
let wordCount = 1;

if (wordCount) {
  console.log("Great! You've started your work!");
} else {
  console.log('Better get to work!');
}


let favoritePhrase = '';

if (favoritePhrase) {
  console.log("This string doesn't seem to be empty.");
} else {
  console.log('This string is definitely empty.');
}
```

# Truthy and Falsy Assignment

```
let username = '';
let defaultName;

if (username) {
  defaultName = username;
} else {
  defaultName = 'Stranger';
}

console.log(defaultName); // Prints: Stranger
```

```
let username = '';
let defaultName = username || 'Stranger';

console.log(defaultName); // Prints: Stranger
```

```
let tool = 'marker';

// Use short circuit evaluation to assign  writingUtensil variable below:
let writingUtensil = tool || 'pen';

console.log(`The ${writingUtensil} is mightier than the sword.`);
```

# Ternary Operator

```
let isNightTime = true;

if (isNightTime) {
  console.log('Turn on the lights!');
} else {
  console.log('Turn off the lights!');
}
```

```
isNightTime ? console.log('Turn on the lights!') : console.log('Turn off the lights!');
```

```
let isLocked = false;

isLocked ?
  console.log('You will need a key to open the door.') : console.log('You will not need a key to open the door.');


let isCorrect = true;

isCorrect? 
  console.log('Correct!')
:  console.log('Incorrect!');


let favoritePhrase = 'Love That!';

favoritePhrase === 'Love That!'?
  console.log('I love that!') :
  console.log("I don't love that!");
```

# Else If Statements

```
let season = 'summer';

if (season === 'spring') {
  console.log('It\'s spring! The trees are budding!');
} else if (season === 'winter'){
  console.log('It\'s winter! Everything is covered in snow.')
} else if (season === 'fall'){
  console.log('It\'s fall! Leaves are falling!')
} else if (season === 'summer'){
  console.log('It\'s sunny and warm because it\'s summer!')
} else {
  console.log('Invalid season.');
}
```

# switch statement

```
let groceryItem = 'papaya';

switch (groceryItem) {
  case 'tomato':
    console.log('Tomatoes are $0.49');
    break;
  case 'lime':
    console.log('Limes are $1.49');
    break;
  case 'papaya':
    console.log('Papayas are $1.29');
    break;
  default:
    console.log('Invalid item');
    break;
}

// Prints 'Papayas are $1.29'
```