const delay = ms => new Promise(res => setTimeout(res, ms));

function test() {
    console.log("Pendiente...");
}

const ipList = [
    "10.81.66.189",
    "10.81.66.161",
    "10.186.129.58"
];

const portList = [
    "5500",
    "5502",
    "5505"
];

// Cambiar segun las necesidades
const ipDirection = ipList[1]
const port = portList[0]
const usePort = true;

let ip = "http://" + ipDirection;

if(usePort) {
    ip += ":" + port
}

export {ip, delay, test};