function solution(input){
    let n = parseInt(input);
    answer = (Math.pow(2,n)+1)**2;
    
    console.log(answer);
}

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input;

rl.on("line", function(line){
    input = line;
    rl.close();

}).on("close", function(){
    solution(input);
    process.exit();
})