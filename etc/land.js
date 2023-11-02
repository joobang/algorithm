
function solution(cells) {
    var answer = -1;
    let userMap = new Map();
    for(let i = 0; i<cells.length; i++){
        for(let j = 0; j<cells[i].length; j++){
            if(!userMap.has(cells[i][j])){
                let landArr = Array.from(Array(cells.length), () => Array(cells[i].length).fill(0));
                landArr[i][j] = 1;
                userMap.set(cells[i][j], landArr);
            }else{
                let landArr = userMap.get(cells[i][j]);
                landArr[i][j] = 1;
                userMap.set(cells[i][j], landArr);
            }
        }
    }
    console.log(userMap);

    for(let [key, val] of userMap){
        let landArr = val;

    }

    return answer;
}

solution([['A','A','A','A','A'],['A','C','C','C','A'],['A','C','C','C','A'],['A','C','C','C','A'],['A','C','C','C','A']])