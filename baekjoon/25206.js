function solution(inputs){
    // sum(학점 * 과목평점)/학점총점
    let sum_subject = 0;
    let sum = 0;
    for(let i = 0; i<inputs.length; i++){
        let [sub, point, grade] = inputs[i].split(' ');
        if(grade != 'P'){
            let grade_point = 0.0;
            if(grade == 'A+') grade_point = 4.5;
            else if(grade == 'A0') grade_point = 4.0;
            else if(grade == 'B+') grade_point = 3.50;
            else if(grade == 'B0') grade_point = 3.0;
            else if(grade == 'C+') grade_point = 2.5;
            else if(grade == 'C0') grade_point = 2.0;
            else if(grade == 'D+') grade_point = 1.5;
            else if(grade == 'D0') grade_point = 1.0;
            else if(grade == 'F') grade_point = 0.0;

            sum_subject += parseFloat(point) * grade_point;
            sum += parseFloat(point);
        }
    }
    //console.log(sum_subject, sum);
    console.log((sum_subject/sum).toFixed(6));
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
    
    inputs.push(line);
    currentLine++;
    if (currentLine > 19) {
        rl.close();
    }

}).on("close", function(){
    solution(inputs);
    process.exit();
})