function solution(inputs){
    //console.log(inputs)
    let rem_arr = [25,10,5,1];
    for(let i = 0; i<inputs.length; i++){
        let answer = "";
        let n = parseInt(inputs[i]);
        for(let j = 0; j<rem_arr.length; j++){
            let quo = Math.floor(n / rem_arr[j]);
            let rem = n % rem_arr[j];
            n = rem;
            if(j == 0){
                answer += quo;
            }else{
                answer = answer + " " + quo;
            }
        }
        console.log(answer);
    }
}

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputs = [];
let totalLines = 0;
let currentLine = 0;

rl.on("line", function(line){
    if(currentLine === 0) {
        // 첫 줄에서 전체 줄 수를 설정
        totalLines = parseInt(line);
    } else {
        inputs.push(line);
    }
    currentLine++;
    if (currentLine > totalLines) {
        rl.close();
    }

}).on("close", function(){
    solution(inputs);
    process.exit();
})