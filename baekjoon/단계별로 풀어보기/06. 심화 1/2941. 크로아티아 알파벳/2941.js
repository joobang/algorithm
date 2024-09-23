function solution(input){

    let alpa = ['c=','c-','dz=','d-','lj','nj','s=','z='];

    let findAlpa = (s,c) =>{
        //console.log(s,c);
        for(let i = 0; i<alpa.length; i++){
            if(s.indexOf(alpa[i]) != -1){
                c++;
                s = s.replace(alpa[i],' ');
                return findAlpa(s,c);
            }
        }

        return [s,c];
    }
    
    let temp = findAlpa(input,0);
    let repl = temp[0].replaceAll(' ','');
    let input_arr = repl.split('');
    console.log(temp[1] + input_arr.length);
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