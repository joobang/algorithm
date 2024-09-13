/**
 * price - 티켓의 가격["A 1", "B 2", "C 3", "D 4"]
 * roll - 새로고침 비용
 * money - 지갑 총 금액
 * shop - 상점 목록[["A","B","B","C"],["A","B","B","C"],["A","B","B","C"]]
 *
 * 3개 중복일때 1점을 획득한다고 할때 최대 가진 돈에서 최대 점수를 얻는 방법
 */

const solution = (price, roll, money, shop) => {
  const priceMap = price.reduce((acc, val) => {
    const splitVal = val.split(" ");
    acc.set(splitVal[0], Number(splitVal[1]));
    return acc;
  }, new Map());

  let maxPoints = 0;
  const memo = new Set();

  const dfs = (shopIndex, remainingMoney, ownedItems, points, shopItems) => {
    // 최대 점수 업데이트
    if (points > maxPoints) maxPoints = points;

    // 예산 초과 또는 상점 끝에 도달하면 종료
    if (remainingMoney < 0) return;

    if (shopIndex >= shop.length && shopItems.length === 0) {
      // 모든 상점을 방문했고 구매할 아이템이 없으면 종료
      return;
    }

    // 메모이제이션 키 생성
    const stateKey = `${shopIndex}-${remainingMoney}-${JSON.stringify(
      ownedItems
    )}-${points}-${shopItems.join(",")}`;

    // 이미 방문한 상태이면 종료
    if (memo.has(stateKey)) return;
    memo.add(stateKey);

    if (shopItems.length > 0) {
      // 현재 아이템을 구매하거나 구매하지 않는 두 가지 경우의 수 탐색
      const item = shopItems[0];
      const itemCost = priceMap.get(item);
      const remainingShopItems = shopItems.slice(1);

      // 아이템을 구매하는 경우
      if (remainingMoney >= itemCost) {
        const newOwnedItems = { ...ownedItems };
        newOwnedItems[item] = (newOwnedItems[item] || 0) + 1;
        let newPoints = points;

        // 아이템이 3개 모이면 점수 획득
        if (newOwnedItems[item] === 3) {
          newPoints += 1;
          newOwnedItems[item] = 0;
        }

        dfs(
          shopIndex,
          remainingMoney - itemCost,
          newOwnedItems,
          newPoints,
          remainingShopItems
        );
      }

      // 아이템을 구매하지 않는 경우
      dfs(shopIndex, remainingMoney, ownedItems, points, remainingShopItems);
    } else {
      // 상점을 새로고침하여 다음 상점으로 이동하는 경우
      if (shopIndex + 1 < shop.length && remainingMoney >= roll) {
        dfs(
          shopIndex + 1,
          remainingMoney - roll,
          ownedItems,
          points,
          shop[shopIndex + 1]
        );
      }
      // 더 이상 이동할 상점이 없으면 종료
    }
  };

  dfs(0, money, {}, 0, shop[0]);

  console.log(`최대 점수: ${maxPoints}`);
  return maxPoints;
};

// 2개
solution(["A 1", "B 2", "C 3", "D 4"], 10, 30, [
  ["A", "B", "B", "C"],
  ["A", "B", "C", "C"],
  ["A", "B", "B", "B"],
]);

// 4개
solution(["A 1", "B 2", "C 3", "D 4"], 2, 30, [
  ["A", "B", "B", "C"],
  ["A", "B", "C", "C"],
  ["A", "B", "B", "B"],
]);
