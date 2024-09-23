function solution(inputs){

    //console.log(inputs)
    let cnt = 0;
    for(let i = 0; i<inputs.length; i++){
        let alpa = new Set();
        let alpa_arr = inputs[i].split('');
        let curr = "";
        let isWord = true;
        for(let j = 0; j<alpa_arr.length; j++){
            if(!alpa.has(alpa_arr[j])){
                alpa.add(alpa_arr[j]);
                curr = alpa_arr[j];
            }else{
                if(curr != alpa_arr[j]){
                    isWord = false;
                    break;
                }
            }
        }

        if(isWord){
            cnt++;
        }
    }

    console.log(cnt);
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