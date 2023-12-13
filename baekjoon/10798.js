function solution(inputs){

   //console.log(inputs);
    let arr = [];
    for(let i = 0; i<inputs.length; i++){
        let line_arr = inputs[i].split('');
        arr.push(line_arr);
    }

    //console.log(arr);
    let answer = "";
    for(let i = 0; i<15; i++){
        if(arr[0].length > i) answer += arr[0][i];
        if(arr[1].length > i) answer += arr[1][i];
        if(arr[2].length > i) answer += arr[2][i];
        if(arr[3].length > i) answer += arr[3][i];
        if(arr[4].length > i) answer += arr[4][i];
    }

    console.log(answer);
}

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputs = [];
let totalLines = 4;
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