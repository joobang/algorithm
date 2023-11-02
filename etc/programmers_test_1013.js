//체스 룩 말놓기
function solution(board){
    let total = board.length;
    
    let temp = [];
    let answer = 0;
    function setRook(arr,row,rowSet,colSet,sum){
        visit= new Array(total).fill(0).map(()=>new Array(total).fill(0));
        if(arr.length === total){
            temp.push([...arr]);
            if(sum > answer ) answer = sum;
            return;
        }
        for(let row = 0; row<total; row++){
            for(let col = 0; col<total; col++){
                if(!rowSet.has(row) && !colSet.has(col)){
                    rowSet.add(row);
                    colSet.add(col);
                    visit[row][col] = 1;
                    setRook([...arr, [row,col]], rowSet,colSet, sum+board[row][col]);
                    rowSet.delete(row);
                    colSet.delete(col);
                }
            }
        }
    }

    setRook([],0,new Set(), new Set(),0, new Array(total).fill(0).map(()=>new Array(total).fill(0)));

}

// 크기 순으로 중 가장 많이 선택되는 방법 배열 찾고 사전식 정렬
function solution(cookies,k){
    let tmep = [];
    let maxLength = 0;
    function setArr(start, arr){
        for(let i = start; i<cookies.length; i++){
            if(arr.length === 0 || arr[arr.lenght-1] < cookies[i]){
                arr.push(cookies[i]);
                setArr(i+1,arr);
                arr.pop();
            }
        }
        if(arr.length === maxLength){
            temp.push([...arr]);
        }else if(arr.length > maxLength){
            temp = [] ;
            temp.push([...arr]);
            maxLength = arr.length;
        }
    }
    setArr(0,[]);
}

// 배열에서 두 요소 뺀 값 중 max 구하기 ( 작은 수 보다 큰 수가 더 뒤에 있는 수여야 한다. )
function solutton(arr){
    let answer = 0;
    return answer;
}
// ㄷ자 부지 선정하기
// 색종이 위에서 붙이기
