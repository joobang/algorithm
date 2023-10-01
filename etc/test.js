/*
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
*/


/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
// var minOperations = function(nums, x) {
//     let list_test = [];
//     let result = nums.length;
//     let isExist = false;
//     for(let i = 0; i<nums.length+1; i++){
//         let leftCnt = i;
//         let rightMax = nums.length - leftCnt;
//         if(leftCnt === 0){
//             for(let j = 1; j<rightMax+1; j++){
//                 let rightArr = nums.slice(-j);
//                 let rightSum = rightArr.reduce((acc,cur) => acc+cur, 0);
//                 if(rightSum === x){
//                     let totalCnt = j;
//                     if(totalCnt < result){
//                         result = totalCnt;
//                     }
//                     isExist = true;
//                 }
//             }
//         }else{
//             for(let j = 0; j<rightMax+1; j++){
//                 list_test.push([i,j]);
//                 let rightArr = nums.slice(-j);
//                 let rightSum = rightArr.reduce((acc,cur) => acc+cur, 0);
//                 let leftArr = nums.slice(i);
//                 let leftSum = leftArr.reduce((acc,cur) => acc+cur, 0);
//                 if(rightSum + leftSum === x){
//                     let totalCnt = i+j;
//                     if(totalCnt < result){
//                         result = totalCnt;
//                     }
//                     isExist = true;
//                 }
//             }
//         }
//     }
//     console.log(list_test);
//     console.log(result);
// };
var minOperations = function(nums, x) {
    let hashMap = new Map();
    let sum = 0;
    let result = nums.length;
    hashMap.set(0,0);
    // 왼쪽 부분 배열의 합을 구하고 해시 맵을 생성
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        if (!hashMap.has(sum)) {
            hashMap.set(sum, i + 1);
        }
    }

    // 합이 x와 같은 부분 배열이 있는 경우
    if (hashMap.has(x)) {
        minOps = hashMap.get(x);
    }

    // 오른쪽 부분 배열의 합을 구하면서 해시 맵을 확인
    sum = 0;
    for (let i = nums.length - 1; i >= 0; i--) {
        sum += nums[i];
        if (hashMap.has(x - sum)) {
            let totalCnt = hashMap.get(x - sum) + nums.length - i;
            if (totalCnt < result){
                result = totalCnt;
            }
        }
    }
    console.log(result);
    console.log(hashMap);
};


minOperations([1,1,4,2,3], 5);