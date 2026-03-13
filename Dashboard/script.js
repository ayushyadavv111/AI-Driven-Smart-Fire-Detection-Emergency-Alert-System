// Dummy sensor values

let temperature = 45
let smoke = 200
let gas = 150

document.getElementById("temp").innerHTML = temperature + " °C"
document.getElementById("smoke").innerHTML = smoke
document.getElementById("gas").innerHTML = gas

if(temperature > 50 || smoke > 300){

document.getElementById("status").innerHTML = "🔥 FIRE RISK"
document.getElementById("status").style.color = "red"

}
else{

document.getElementById("status").innerHTML = "SAFE"
document.getElementById("status").style.color = "green"

}
