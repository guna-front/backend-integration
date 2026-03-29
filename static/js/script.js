function changeTitle(){

let title = document.getElementById("edit");

if(title.innerText === "Welcome to Healthy Fruits"){
title.innerText = "Eat Fruits Daily for a Healthy Life!";
}
else{
title.innerText = "Welcome to Healthy Fruits";
}

}
let video = document.getElementById("fruitVideo"); let music = document.getElementById("bgmusic");
if(video && music){
    music.volume = 0.3;
video.onplay = function(){ music.play(); }
video.onpause = function(){ music.pause(); }
video.onended = function(){ music.pause(); music.currentTime = 0; }
}

let foods = ["Strawberries", "Egg", "Spinach"];
let tableSummary = document.querySelector('.table-summary');
if(tableSummary){
    tableSummary.innerText = "Total foods: " + foods.length;
}




