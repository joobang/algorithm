function solution(clothes) {
  let answer = 1;

  const clothMap = clothes.reduce((acc, val) => {
    const [name, type] = val;
    if (acc.has(type)) {
      acc.get(type).push(name);
    } else {
      acc.set(type, [name]);
    }
    return acc;
  }, new Map());

  for (const [key, value] of clothMap) {
    answer *= value.length + 1;
  }
  return answer - 1;
}
