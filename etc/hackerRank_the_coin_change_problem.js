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
 * Complete the 'getWays' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. LONG_INTEGER_ARRAY c
 */

function getWays(n, c) {
    // 1~n 까지의 수를 동전으로 만들 수 있는 경우의 수를 나타내는 배열
    const ways  = new Array(n + 1).fill(0);
    // 자기 동전으로만 만들 수 있는 수 ways[0]은 1로 초기화
    ways[0] = 1;
    
    // 각 동전을 돌며 1부터 n까지 수를 만들 수 있는지 체
    c.forEach(coin => {
        for (let i = 1; i < ways.length; i++) {
            /* 동전보다 현재 수가 크거나 같은 경우는 i - coin의 수를 만드는 경우의 수와 현재수를 만드는 경우의 수를 더해서 표현가능.
            ex) n=3, c=[1,2,3]
            코인 1로 1~4까지 만들수 있는 경우의 수 [ 1, 1, 1, 1, 1 ]
            코인 1,2로 1~4까지 만들수 있는 경우의 수  [ 1, 1, 2, 2, 3 ]
            코인 1,2,3로 1~4까지 만들수 있는 경우의 수  [ 1, 1, 2, 3, 4 ]
            n=10, c=[2,5,3,6]
            코인 2로 1~10까지 만들수 있는 경우의 수 [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ]
            코인 2,5로 1~10까지 만들수 있는 경우의 수 [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 2 ]
            코인 2,5,3로 1~10까지 만들수 있는 경우의 수 [ 1, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4 ]
            코인 2,5,3,6로 1~10까지 만들수 있는 경우의 수 [ 1, 0, 1, 1, 1, 2, 3, 2, 4, 4, 5 ]
            */
            if (coin <= i) {
                ways[i] += ways[i - coin];
            }
        }
        
    });
    
    return ways[n];
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const m = parseInt(firstMultipleInput[1], 10);

    const c = readLine().replace(/\s+$/g, '').split(' ').map(cTemp => parseInt(cTemp, 10));

    // Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    const ways = getWays(n, c);
    console.log(ways);
    ws.write(ways + '\n');

    ws.end();
}
