/*
LECTURE 6: CODING WITH JAVASCRIPT
*/

// console.log("HELLO IDOK")

var y = 35
let x = 5
const z = 10

console.log(x, y, z)

if (x == y) {
    console.log(x.toString().concat(" is equal to ", y.toString))
} else if (x==z) {
    console.log(x.toString().concat(" is not equal to ", z.toString()))
} else {
    console.log(x.toString().concat(" is not equal to anything "))
}

const players = ["tatum", "brown", "horford"]
console.log(players.length)

console.log(0 == "0")
console.log(0 === "0")

for (var i = 0; i < z; i++){
    console.log(i)
}

console.log(players[2])

function degreesToRadians(num) {
    var value = num * Math.PI/180
    return value
}

console.log(degreesToRadians(180))

function getLatitude(distance, azimuth){
    var latitude = -distance * Math.cos(degreesToRadians(azimuth))
    return latitude
}

console.log(getLatitude(12, 50))