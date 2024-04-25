/*
GE 120
Omar Pesebre
2023-06343
Exercise 3
*/



function getLatitude(distance, azimuth){
    /*
    Determines the latitude of a line

    Input:
    distance - float
    azimuth - float

    Output
    latitude - float
    */

    if (azimuth % 180 == 90) {return 0} else {
    return (-distance * Math.cos(azimuth * Math.PI / 180.0))}
}

function getDeparture(distance, azimuth){
    /*
    Determines the departure of a line

    Input:
    distance - float
    azimuth - float

    Output
    departure - float
    */

    if (azimuth % 180 == 0) {return 0} else {
    return (-distance * Math.sin(azimuth * Math.PI / 180.0)) }
}

function azimuthToBearing(azimuth){
    /*
    Determines the DMS bearing of a line

    Input:
    azimuth - float

    Output
    bearing - string
    */

    azimuth = azimuth % 360
   

    if (azimuth > 0 && azimuth < 90) {
        bearing = 'S '.concat(azimuth.toPrecision(5).toString(), ' W')
    }
    else if (azimuth > 90 && azimuth < 180) {
        bearing = 'N '.concat(180-azimuth.toPrecision(5).toString(), ' W')
    }
    else if (azimuth > 180 && azimuth < 270) {
        bearing = 'N '.concat((azimuth-180).toPrecision(5).toString(), ' E')
    }
    else if (azimuth > 270 && azimuth < 360) {
        bearing = 'S '.concat(3600-azimuth.toPrecision(5).toString(), ' E')
    }
    else if (azimuth == 0) {
        bearing = "DUE SOUTH"
    }
    else if (azimuth == 90) {
        bearing = "DUE WEST"
    }
    else if (azimuth == 180) {
        bearing = "DUE NORTH"
    }
    else if (azimuth == 270) {
        bearing = "DUE EAST"
    }
    else{
        bearing = "NA"
    }
    return bearing
}

var data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562],
]
var lines = []
var sumLat = 0
var sumDep = 0
var sumDist = 0

for (var i = 0; i < data.length; i++) {
    let line = data[i]
    let distance = line[0]
    let azimuth = line[1]

    let bearing = azimuthToBearing(azimuth)
    let lat = getLatitude(distance, azimuth)
    let dep = getDeparture(distance, azimuth)
   
    sumLat += lat
    /* similar to sumLat = sumLat + lat */
    sumDep += dep
    sumDist += distance

    lines.push([(i+1), distance, bearing, lat, dep])
}

//console.log(lines)
console.log(("LINE NO.".padEnd(10), "DISTANCE".padEnd(10), "BEARING".padEnd(15), "LATITUDE".padEnd(10), "DEPARTURE".padEnd(10)))

for (var line of lines) {
    console.log(line[0].toString().padEnd(10), line[1].toString().padEnd(10), line[2].padEnd(15), line[3].toPrecision(5).toString().padEnd(10), line[4].toPrecision(5).toString().padEnd(10))

}
/*get the sum of lat, dep, and distance*/

console.log("SUMMATION OF LAT:", sumLat.toPrecision(5))
console.log("SUMMATION OF DEP:", sumDep.toPrecision(5))
console.log("SUMMATION OF DIST:", sumDist.toPrecision(5))

/*get the LEC, REC, BOSE*/
var lec = Math.sqrt((sumLat ** 2) + (sumDep ** 2))
console.log("LEC:", lec)

rec = sumDist/lec
console.log("1: ", Math.floor(rec/1000)*1000)

BOSE = (Math.atan(Math.abs(sumDep)/Math.abs(sumLat)))

if (sumLat > 0 && sumDep > 0) {
    boSe = 'S '.concat(BOSE.toPrecision(5).toString(), ' W')
}
else if (sumLat < 0 && sumDep > 0) {
    boSe = 'N '.concat(BOSE.toPrecision(5).toString(), ' W')
}
else if (sumLat < 0 && sumDep < 0) {
    boSe = 'N '.concat(BOSE.toPrecision(5).toString(), ' E')
}
else if (sumLat > 0 && sumDep < 0) {
    boSe = 'S '.concat(BOSE.toPrecision(5).toString(), ' E')
}
else {
    boSe = "NA"
}


console.log("BoSE:", boSe)

// get the cLat, cDep, adjLat, adjDep

constCorrLat = -sumLat/sumDist
constCorrDep = -sumDep/sumDist


console.log(("LINE NO.".padEnd(10), "ADJUSTED LATITUDE".padEnd(10), "ADJUSTED DEPARTURE".padEnd(10)))

for (var line of lines) {
    corr_lat = constCorrLat * line [1]
    corr_dep = constCorrDep * line [1]

    adjLat = line [3] + corr_lat
    adjDep = line [4] + corr_dep
    console.log(line[0].toString().padEnd(10), adjLat.toPrecision(5).toString().padEnd(10), adjDep.toPrecision(5).toString().padEnd(10))
}
console.log("ADJUSTED LINES")
console.log(("LINE NO.".padEnd(10), "ADJUSTED DISTANCE".padEnd(10), "ADJUSTED BEARING".padEnd(10)))
for (var line of lines) {
    corr_lat = constCorrLat * line [1]
    corr_dep = constCorrDep * line [1]

    adjLat = line [3] + corr_lat
    adjDep = line [4] + corr_dep

// Obtain the adjusted distance and bearing

    adjDist = Math.sqrt((adjLat ** 2) + (adjDep ** 2))
    adj_bearing = (Math.atan(Math.abs(adjDep)/Math.abs(adjLat)))
    if (adjLat > 0 && adjDep > 0) {
        adjBearing = 'N '.concat(adj_bearing.toPrecision(5).toString(), ' E')
    }
    else if (adjLat < 0 && adjDep > 0) {
        adjBearing = 'S '.concat(adj_bearing.toPrecision(5).toString(), ' E')
    }
    else if (adjLat < 0 && adjDep < 0) {
        adjBearing = 'S '.concat(adj_bearing.toPrecision(5).toString(), ' W')
    }
    else if (adjLat > 0 && adjDep < 0) {
        adjBearing = 'N '.concat(adj_bearing.toPrecision(5).toString(), ' W')
    }
    else {
        adjBearing = "NA"
    }

    console.log((line[0].toString().padEnd(10), adjDist.toPrecision(5).toString().padEnd(10), adjBearing.padEnd(15)))


}
console.log("--------END--------")