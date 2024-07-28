const departTripTicket = {
  name: "Martijn",
  from: "Meppel, Drenthe",
  to: "London, England",
  businessClass: false,
  upgrade() {
    if (departTripTicket.businessClass) {
      console.log("Your ticket is already business class!");
    } else {
      departTripTicket.businessClass = true;
    }
  }
}

const returnTripTicket = {
  name: "Martijn",
  from: "London, England",
  to: "Meppel, Drenthe",
  businessClass: true,
  upgrade() {
    if (returnTripTicket.businessClass) {
      console.log("Your ticket is already business class!");
    } else {
      returnTripTicket.businessClass = true;
    }
  }
}

departTripTicket.upgrade();
returnTripTicket.upgrade();

// Bonus Section

departTripTicket.leaveTime = 12;
departTripTicket.arriveTime = 23;
departTripTicket.flightTime = function() {
  let flightTime = departTripTicket.arriveTime - departTripTicket.leaveTime;
  if (flightTime < 0) {
    flightTime = flightTime * -1;
  }
  console.log(flightTime + " hours")
}

returnTripTicket.leaveTime = 24;
returnTripTicket.arriveTime = 4;
returnTripTicket.flightTime = function() {
  let flightTime = returnTripTicket.arriveTime - returnTripTicket.leaveTime;
  if (flightTime < 0) {
    flightTime = flightTime * -1;
  }
  console.log(flightTime + " hours")
}

departTripTicket.flightTime();
returnTripTicket.flightTime();
