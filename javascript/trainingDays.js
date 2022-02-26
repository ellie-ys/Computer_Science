// The scope of `random` is too loose
const random = Math.floor(Math.random() * 3);

const getRandEvent = () => {
  if (random === 0) {
    return "Marathon";
  } else if (random === 1) {
    return "Triathlon";
  } else if (random === 2) {
    return "Pentathlon";
  }
};

// The scope of `days` is too tight
const event = getRandEvent();
const getTrainingDays = event => {
  let days = 0;
  if (event === "Marathon") {
    days = 50;
    return days;
  } else if (event === "Triathlon") {
    days = 100;
    return days;
  } else if (event === "Pentathlon") {
    days = 200;
    return days;
  }
  return days;
};
console.log(getTrainingDays(event));

// The scope of `name` is too tight
const logEvent = (name, event) => {
  console.log(`${name}'s event is: ${event}`);
};

const logTime = (name, days) => {
  console.log(`${name}'s time to train is: ${days} days`);
};

const days = getTrainingDays(event);
const name = "Nala";
// Define a `name` variable. Use it as an argument after updating logEvent and logTime

logEvent(name, event);
logTime(name, days);

//use another program but same event
const event2 = getRandEvent();
const days2 = getTrainingDays(event2);
const name2 = "Warren";

logEvent(name2, event2);
logTime(name2, days2);
