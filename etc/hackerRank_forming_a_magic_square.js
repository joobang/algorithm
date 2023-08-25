'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];h
}

/*
 * Complete the 'formingMagicSquare' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY s as parameter.
 */

function formingMagicSquare(s) {
    // Write your code here
    //console.log(s)
    let magicSquare_list = [];
    magicSquare_list.push([[8,1,6],[3,5,7],[4,9,2]]);
    magicSquare_list.push([[6,1,8],[7,5,3],[2,9,4]]);
    magicSquare_list.push([[4,9,2],[3,5,7],[8,1,6]]);
    magicSquare_list.push([[2,9,4],[7,5,3],[6,1,8]]);
    magicSquare_list.push([[4,3,8],[9,5,1],[2,7,6]]);
    magicSquare_list.push([[2,7,6],[9,5,1],[4,3,8]]);
    magicSquare_list.push([[8,3,4],[1,5,9],[6,7,2]]);
    magicSquare_list.push([[6,7,2],[1,5,9],[8,3,4]]);
    
    let minCost = 36;
    for(let z = 0; z<magicSquare_list.length; z++){
        let currCost = 0;
        let currSquare = magicSquare_list[z]
        for(let i = 0; i<3; i++){
            for(let j = 0; j<3; j++){
                currCost += Math.abs(currSquare[i][j] - s[i][j]);
            }
        }       
        if(currCost < minCost){
            minCost = currCost
        }
    }
    
    return minCost;
    
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let s = Array(3);

    for (let i = 0; i < 3; i++) {
        s[i] = readLine().replace(/\s+$/g, '').split(' ').map(sTemp => parseInt(sTemp, 10));
    }

    const result = formingMagicSquare(s);

    ws.write(result + '\n');

    ws.end();
}
