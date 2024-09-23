function solution(input){
    let [n, b] = input.split(' ');
    let n_arr = n.split('');
    let jisu = 0;
    let answer = 0;
    while(n_arr.length > 0){
        //console.log(n_arr,answer);
        let square = 1;
        for(let i = 0; i<jisu; i++){
            square *= parseInt(b);
        }
        
        let pop_n = n_arr.pop();
        if(pop_n == "A") answer += square * 10
        else if(pop_n == "B") answer += square * 11
        else if(pop_n == "C") answer += square * 12
        else if(pop_n == "D") answer += square * 13
        else if(pop_n == "E") answer += square * 14
        else if(pop_n == "F") answer += square * 15
        else if(pop_n == "G") answer += square * 16
        else if(pop_n == "H") answer += square * 17
        else if(pop_n == "I") answer += square * 18
        else if(pop_n == "J") answer += square * 19
        else if(pop_n == "K") answer += square * 20
        else if(pop_n == "L") answer += square * 21
        else if(pop_n == "M") answer += square * 22
        else if(pop_n == "N") answer += square * 23
        else if(pop_n == "O") answer += square * 24
        else if(pop_n == "P") answer += square * 25
        else if(pop_n == "Q") answer += square * 26
        else if(pop_n == "R") answer += square * 27
        else if(pop_n == "S") answer += square * 28
        else if(pop_n == "T") answer += square * 29
        else if(pop_n == "U") answer += square * 30
        else if(pop_n == "V") answer += square * 31
        else if(pop_n == "W") answer += square * 32
        else if(pop_n == "X") answer += square * 33
        else if(pop_n == "Y") answer += square * 34
        else if(pop_n == "Z") answer += square * 35
        else{
            answer += square * parseInt(pop_n);
        }
        jisu++;
        
    }

    console.log(answer);
    
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