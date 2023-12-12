function solution(inputs){
    
    let arr = new Array(9).fill(0).map(() => new Array(9));
    let max = 0;
    let max_index = "1 1";
    for(let i = 0; i<9; i++){
        let numbers = inputs[i].split(" ").map((a) => parseInt(a));
        //console.log(numbers);
        for(let j = 0; j<9; j++){
            if(max < numbers[j]){
                max = numbers[j];
                max_index = (i+1) + " " + (j+1);
            }
        }
    }

    console.log(max);
    console.log(max_index);
    
}

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputs = [];
let totalLines = 8;
let currentLine = 0;

rl.on("line", function(line){
    inputs.push(line);
    currentLine++;
    if (currentLine > totalLines) {
        rl.close();
    }

}).on("close", function(){
    solution(inputs);
    process.exit();
})