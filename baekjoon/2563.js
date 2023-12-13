function solution(inputs){

    //console.log(inputs)
    let square = new Array(101).fill(0).map(() => new Array(101));
    let area = 0;

    for(let i = 0; i<inputs.length; i++){
        let [n,m] = inputs[i].split(' ');
        for(let j = parseInt(n); j<parseInt(n)+10; j++){
            for(let z = parseInt(m); z<parseInt(m)+10; z++){
                if(!square[j][z]) {
                    //console.log(j,z);
                    square[j][z] = 1;
                    area += 1;
                }
            }
        }
    }

    console.log(area);
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