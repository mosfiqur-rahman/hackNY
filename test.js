var fs = require("fs");
var text = fs.readFileSync("./lat.txt");
var latByLine = text.toString().split("\n");
console.log(latByLine[0]);
