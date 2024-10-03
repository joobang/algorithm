/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  // 시작, 끝, 타겟
  return binarySearch(0, nums.length - 1, target, nums);
};

var binarySearch = function (start, end, target, nums) {
  // 중간이랑 비교하고 같으면 끝.
  // 중간이랑 비교하고 중간보다 작으면 시작부터 중간까지로 다시 재귀
  // 중간이랑 비교하고 중간보다 크면 중간부터 끝까지 다시 재귀
  if (start > end) {
    return -1; // 타겟을 찾지 못한 경우
  }

  // 현재 검색 범위의 중간 인덱스를 계산합니다.
  const mid = Math.floor((start + end) / 2);

  if (nums[mid] === target) {
    return mid;
  }
  // 중간 값이 타겟보다 크면, 타겟은 왼쪽 절반에 있을 수 있으므로 왼쪽 범위로 재귀 호출합니다.
  else if (nums[mid] > target) {
    return binarySearch(start, mid - 1, target, nums);
  }
  // 중간 값이 타겟보다 작으면, 타겟은 오른쪽 절반에 있을 수 있으므로 오른쪽 범위로 재귀 호출합니다.
  else {
    return binarySearch(mid + 1, end, target, nums);
  }
};
