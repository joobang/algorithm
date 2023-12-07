function solution(input){
    let re_str = input.split('').reverse().join('');
    
    //let test = Array.from({length: 2}, () => Array.from({length:2}, () => 0));
    //const  arr = Array.from(new Array(columns), () => new Array(rows).fill(0));
    
    if(input === re_str){
        console.log(1);
    }else{
        console.log(0);
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