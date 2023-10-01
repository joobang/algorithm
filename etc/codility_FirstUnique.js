function solution(A) {
    // Implement your solution here
    let lowest = -1;
    let numMap = new Map();
    for(let i = 0; i<A.length; i++){
        if(!numMap.has(A[i])){
            numMap.set(A[i], 1);
        }else{
            numMap.set(A[i], numMap.get(A[i])+1);
        }
    }

    for(const [key, value] of numMap){
        if(value === 1){
            lowest = key;
            break;
        }
    }

    return lowest;
}
