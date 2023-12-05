// //한 줄의 입력(띄어쓰기 o , 예를 들면 1 2 3 4 5)
// function solution(input){
//     const [a,b] = input;
//     const answer = a+b;
//     console.log(answer);
// }

// const readline = require('readline');
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });
// let input;
// let list = [];
// rl.on('line', function(line) {
//     input = line;
//     rl.close();
// }).on("close", function() {
//     // list = input.split(' ').map((el) => el); 
//     list = input.split(' ').map((el) => parseInt(el)); // 입력값이 정수라면 parseInt로 형 변환
//     solution(list);
//     process.exit();
// });

//한 개의 입력(띄어쓰기x)
function solution(input){
    let total = 2*input-1
    let answer = ""
    for(let i = 1; i < total+1; i++){
        let sub = 2*i-1
        let star = ""
        if(input < i){
            let temp = (i - input)
            sub = 2*(input-temp)-1
            for(let j = 0; j < temp; j++){
                star += " "
            }
            for(let j = 0; j < sub; j++){
                star += "*"
            }
        }else{
            let temp = (input - i)
            sub = 2*i-1
            for(let j = 0; j < temp; j++){
                star += " "
            }
            for(let j = 0; j < sub; j++){
                star += "*"
            }
        }
        answer = answer + star + "\n"
    }
    console.log(answer)
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