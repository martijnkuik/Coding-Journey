const car = { 
  model: "Ford",
  year: 2019,
  color: "Black", 
  used: true

}

if (car.used) {
  console.log("I want a " + car.year + " " + car.model + " that is used.")
} else {
  console.log("I want a " + car.year + " " + car.model + " that is new.")
}
