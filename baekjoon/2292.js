function solution(input){
    let n = parseInt(input);
    //console.log(n);
    let i = 0;
    
    while(n > (i*(i+1)/2)*6 + 1){
        console.log(n, (i*(i+1)/2)*6 + 1);
        i++;
        
    }
    console.log(i+1);
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