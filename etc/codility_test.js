// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(inner, outer, points_x, points_y) {
    // Implement your solution here
    // two point distance root (x2-x1)^2 + (y2-y1)^2
    let result = [];
    for(let i = 0; i<points_x.length; i++){
        //console.log(points_x[i], points_y[i]);
        let x_distance = points_x[i] * points_x[i];
        let y_distance = points_y[i] * points_y[i];
        let distance = Math.sqrt(x_distance + y_distance);
        //console.log(distance);
        if(distance > inner && distance < outer){
            result.push([points_x[i], points_y[i]]);
        }
    }
    //console.log(result);
    return result.length;
}


// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(D, T) {
    // Implement your solution here
    // p task , g task, m task, lastIndex 
    let p_task = 0, g_task = 0, m_task = 0;
    let p_lastIdx = -1, g_lastIdx = -1, m_lastIdx = -1;
    
    // 구간별 합계를 위한 map
    let sumMap = new Map();

    // 분리수거 별 시간 계산
    for(let i=0; i<D.length; i++){
        let taskArr = T[i].split('');
        sumMap.set(i, sumMap.has(i-1) ? sumMap.get(i-1)+D[i] : D[i]);
        if(taskArr.length > 0){
            for(let j=0; j<taskArr.length; j++){
                if(taskArr[j] === 'P'){
                    p_task += 1;
                    p_lastIdx = i;
                }
                if(taskArr[j] === 'G'){
                    g_task += 1;
                    g_lastIdx = i;
                }
                if(taskArr[j] === 'M'){
                    m_task += 1;
                    m_lastIdx = i;
                }
            }
        }
        
    }

    // 거리 별 시간계산
    if(p_lastIdx !== -1) p_task += sumMap.get(p_lastIdx)*2;
    if(g_lastIdx !== -1) g_task += sumMap.get(g_lastIdx)*2;
    if(m_lastIdx !== -1) m_task += sumMap.get(m_lastIdx)*2;
    
    //console.log(sumMap);
    //console.log(p_task,g_task,m_task);
    return Math.max(p_task, g_task, m_task);
}


// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S, T) {
    // Implement your solution here
    //let result = [];
    let result = 0;
    
    let start_dt = new Date();
    let end_dt = new Date();
    let start_arr = S.split(':');
    let end_arr = T.split(':');
    start_dt.setHours(parseInt(start_arr[0]),start_arr[1],start_arr[2]);
    end_dt.setHours(parseInt(end_arr[0]),end_arr[1], end_arr[2]);
    
    let start_time = start_dt.getTime();
    let end_time = end_dt.getTime();
    while(start_time <= end_time){
        let currDate = new Date(start_time);
        let currSet = new Set();

        let currHours = String(currDate.getHours()).padStart(2, '0');
        let currMinutes = String(currDate.getMinutes()).padStart(2, '0');
        let currSeconds = String(currDate.getSeconds()).padStart(2, '0');

        let currTimeString = currHours+currMinutes+currSeconds;
        for(let i = 0; i<currTimeString.length; i++){
            if(!currSet.has(currTimeString[i])){
                currSet.add(currTimeString[i]);
            }
        }

        if(currSet.size <= 2){
            //let curr_dt = currHours + ':' + currMinutes + ':' + currSeconds;
            //result.push(curr_dt);
            result++;
        }
        start_time += 1000;
    }
    return result;
}
