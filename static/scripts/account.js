<<<<<<< HEAD
var apiBox = document.getElementById("api-key");
var generateButton = document.getElementById("generate-api");
var clearButton = document.getElementById("clear-api");

function generateAPI(){
    var api = Math.random()*10000;
    apiBox.setAttribute("placeholder", api);
}

function clearAPI(){
    apiBox.removeAttribute("placeholder");
=======
var apiBox = document.getElementById("api-key");
var generateButton = document.getElementById("generate-api");
var clearButton = document.getElementById("clear-api");

function generateAPI(){
    var api = Math.random()*10000;
    apiBox.setAttribute("placeholder", api);
}

function clearAPI(){
    apiBox.removeAttribute("placeholder");
>>>>>>> 62f8a435b7cefe3a15277dea784a9323c28c2531
}