import { ip, goURL } from "./common.js";

document.getElementById("mc-button-store").addEventListener("click", function () {
    goURL(ip + "/store");
    console.log(ip + "/store");
});