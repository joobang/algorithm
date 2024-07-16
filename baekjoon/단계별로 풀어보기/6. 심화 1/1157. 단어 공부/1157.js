function solution(input){
    let input_arr = input.split('');
    let temp = new Map()
    for(let i = 0; i<input_arr.length; i++){
        let alpa = input_arr[i].toUpperCase();
        if(!temp.has(alpa)){
            temp.set(alpa, 1);
        }else{
            temp.set(alpa, temp.get(alpa)+1);
        }
    }
    temp = new Map([...temp].sort((a,b) => b[1] - a[1]));
    
    let sort_arr = [...temp]
    let answer = "?"
    let max = 0

    //console.log(answer, max,sort_arr)
    for(const [key, val] of sort_arr){
        if(val > max){
            answer = key;
            max = val;
        }else if(val == max){
            answer = "?";
            break;
        }
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