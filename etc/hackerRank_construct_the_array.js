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
    return inputString[currentLine++];
}

/*
 * Complete the 'countArray' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER x
 */

function countArray(n, k, x) {
    // Return the number of ways to fill in the array.
    /*
        
        a는 x의 개수의 배열
        b는 x가 아닌 수의 배열
        연속된 수가 올 수 없다는 조건을 사용하면 n의 개수와 k의 개수에 따라 반복적인
        a[n], b[n]의 값을 찾을 수 있다.

        n=4, k=3, x=2 의 경우로 보면
        1부터 무조건 시작하고 만들 수 있는 모든 경우의 수는 다음과 같다.
        1 -> 2 -> 1 -> 2
                    -> 3
               -> 3 -> 1
                    -> 2
          -> 3 -> 1 -> 2
                    -> 3
               -> 2 -> 1
                    -> 3
        
        a는 x의 개수의 배열이고 b는 x가 아닌 수의 배열이므로
        a[0]은 x가 0개 이므로 0, b[0]은 x가 1개 이므로 1
        a[1]은 x가 1개 이므로 1, b[1]은 x가 1개 이므로 1
        ...
        다음과 같은 규칙으로 아래와 같은 식을 만들 수 있다.
        x의 개수배열
        a[i] = b[i-1]
        
        x가 아닌 수 개수
        x가 아닌 수 = 이전 x의 수 * x를 제외한 k의 수 + 이전 x가 아닌 수 * x와 x가 아닌(연속된) 수를 제외한 k의 수
        b[i] = a[i-1]*(k-1) + b[i-1]*(k-2)

        x가 1일 때는 a[0],b[0]이 1,0이 된다.
    
    */
    let a = new Array(n).fill(0);
    let b = new Array(n).fill(0);
    
    a[0] = x != 1 ? 0 : 1;
    b[0] = x != 1 ? 1 : 0;
    
    for(let i=1; i<n; i++){
        a[i] = b[i-1] % (10**9 + 7);
        b[i] = (a[i-1]*(k-1) + b[i-1]*(k-1-1)) % (10**9 + 7);
    }
    
    return a[n-1]
 }

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const k = parseInt(firstMultipleInput[1], 10);

    const x = parseInt(firstMultipleInput[2], 10);

    const answer = countArray(n, k, x);

    ws.write(answer + '\n');

    ws.end();
}
