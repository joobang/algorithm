function solution(input){
    let [n, b] = input.split(' ');
    let jisu = 0;
    let answer = "";
    
    let x = parseInt(n);
    while(x > 0){
        let quo = Math.floor(x / parseInt(b));
        let rem = x % parseInt(b);
        x = quo;
        
        if(rem == 10) answer = "A" + answer;
        else if(rem == 11) answer = "B" + answer;
        else if(rem == 12) answer = "C" + answer;
        else if(rem == 13) answer = "D" + answer;
        else if(rem == 14) answer = "E" + answer;
        else if(rem == 15) answer = "F" + answer;
        else if(rem == 16) answer = "G" + answer;
        else if(rem == 17) answer = "H" + answer;
        else if(rem == 18) answer = "I" + answer;
        else if(rem == 19) answer = "J" + answer;
        else if(rem == 20) answer = "K" + answer;
        else if(rem == 21) answer = "L" + answer;
        else if(rem == 22) answer = "M" + answer;
        else if(rem == 23) answer = "N" + answer;
        else if(rem == 24) answer = "O" + answer;
        else if(rem == 25) answer = "P" + answer;
        else if(rem == 26) answer = "Q" + answer;
        else if(rem == 27) answer = "R" + answer;
        else if(rem == 28) answer = "S" + answer;
        else if(rem == 29) answer = "T" + answer;
        else if(rem == 30) answer = "U" + answer;
        else if(rem == 31) answer = "V" + answer;
        else if(rem == 32) answer = "W" + answer;
        else if(rem == 33) answer = "X" + answer;
        else if(rem == 34) answer = "Y" + answer;
        else if(rem == 35) answer = "Z" + answer;
        else{
            answer = rem + answer;
        }

        
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