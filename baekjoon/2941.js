function solution(input){
    let input_arr = input.split('');
    let cnt = 0

    let alpa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    let pos = 0
    while(pos !== -1){
        for(let i = 0; i<alpa.length; i++){
            if(input.indexOf(alpa[i]) != -1){
                cnt++;
                input = input.replace(alpa[i],'');
            }
        }
    }
}

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input;
rl.on("line", function(line){
    input = line;
    // input = parseInt(line); // 입력 값이 정수라면 parseInt로 형변환
    rl.close();
}).on("close", function(){
    solution(input);
    process.exit();
})