function solution(input){
    let n = parseInt(input);
    let d = 1;
    while(d*(d+1)/2 < n){
        d++;
    }
    let end = d*(2 + (d-1))/2;
    let start = end - d + 1;
    let target = start;
    if(d % 2 == 0){
        let x = 1, y = d;
        for(let i = 0; i<d; i++){
            if(target == n){
                console.log(x +"/"+ y);
                break;
            }
            target += 1;
            x += 1;
            y -= 1;
        }
    }else{
        let x = d, y = 1;
        for(let i = 0; i<d; i++){
            if(target == n){
                console.log(x +"/"+ y);
                break;
            }
            target += 1;
            x -= 1;
            y += 1;
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
    rl.close();

}).on("close", function(){
    solution(input);
    process.exit();
})