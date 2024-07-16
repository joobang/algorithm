function solution(n,m,inputs){
    
    //console.log(n,m,inputs);
    for(let i = 0; i<n; i++){
        
        let answer = ""
        let a_arr = inputs[i].split(" ");
        let b_arr = inputs[i+n].split(" ");
        ///console.log(a_arr,b_arr);
        for(let j = 0; j<m; j++){
            if(j == 0){
                //console.log(parseInt(a_arr[j]) , parseInt(b_arr[j]))
                answer += parseInt(a_arr[j]) + parseInt(b_arr[j]);
            }else{
                ///console.log(parseInt(a_arr[j]) , parseInt(b_arr[j]))
                answer += " " + (parseInt(a_arr[j]) + parseInt(b_arr[j]));
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
let n,m;

rl.on("line", function(line){
    if(currentLine === 0) {
        // 첫 줄에서 전체 줄 수를 설정
        [n,m] = line.split(' ');
        
        totalLines = parseInt(n)*2;
    } else {
        inputs.push(line);
    }
    currentLine++;
    if (currentLine > totalLines) {
        rl.close();
    }

}).on("close", function(){
    solution(parseInt(n),parseInt(m),inputs);
    process.exit();
})