function solution(inputs) {
  const chessboard = inputs.map((c) => c.split(""));

  let min = chessboard.length * chessboard[0].length;
  for (let i = 0; i < chessboard.length; i++) {
    for (let j = 0; j < chessboard[i].length; j++) {
      const current = getMinChangeChess(chessboard, i, j);
      if (current < min) {
        min = current;
      }
    }
  }
  console.log(min);
  // console.log(getMinChangeChess(chessboard, 0, 5));
}

function getMinChangeChess(chessboard, i, j) {
  const chessboardLine = chessboard.length;
  const chessLine = chessboard[0].length;
  // i, j는 8 * 8 체스판의 시작점
  // i + 7, j + 7이 존재해야 만들수 있음 ->
  // chessboardLine - 1 >= i + 7, chessLine - 1 >= j + 7 항상 만족
  // i, j는 8 * 8 체스판의 시작점
  if (chessboardLine - 1 >= i + 7 && chessLine - 1 >= j + 7) {
    let changeNumber1 = 0; // 첫 번째 패턴: 첫 칸을 기준으로 번갈아가며 체크
    let changeNumber2 = 0; // 두 번째 패턴: 첫 칸의 반대 패턴으로 체크
    let firstChess = chessboard[i][j]; // 시작하는 체스판의 첫 번째 칸 값 (B 또는 W)

    for (let y = i; y < i + 8; y++) {
      for (let x = j; x < j + 8; x++) {
        const currentChess = chessboard[y][x]; // 현재 칸의 값

        // 첫 번째 패턴: 첫 번째 칸과 짝수/홀수 패턴이 일치해야 함
        if ((y + x) % 2 === 0) {
          // y + x가 짝수인 좌표는 첫 번째 칸과 같아야 함
          if (currentChess !== firstChess) {
            changeNumber1++; // 같지 않으면 변경 필요
          }
        } else {
          // y + x가 홀수인 좌표는 첫 번째 칸과 달라야 함
          if (currentChess === firstChess) {
            changeNumber1++; // 같으면 변경 필요
          }
        }

        // 두 번째 패턴: 첫 번째 칸과 반대되는 패턴
        if ((y + x) % 2 === 0) {
          // y + x가 짝수인 좌표는 첫 번째 칸과 달라야 함
          if (currentChess === firstChess) {
            changeNumber2++; // 같으면 변경 필요
          }
        } else {
          // y + x가 홀수인 좌표는 첫 번째 칸과 같아야 함
          if (currentChess !== firstChess) {
            changeNumber2++; // 같지 않으면 변경 필요
          }
        }
      }
    }

    // 두 패턴 중 더 적은 변경 횟수를 반환
    return Math.min(changeNumber1, changeNumber2);
  } else {
    return chessboardLine * chessLine; // 조건에 맞지 않으면 큰 값 반환
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let totalLines = 0;

let currentLine = 0;
let inputs = [];

rl.on("line", function (line) {
  if (currentLine === 0) {
    // 첫 줄에서 숫자를 가져와 총 받을 라인 수를 설정
    totalLines = parseInt(line.split(" ")[0]);
  } else {
    inputs.push(line); // 나머지 입력을 배열에 저장
  }
  currentLine++;

  // 설정한 줄 수만큼 받으면 종료
  if (currentLine > totalLines) {
    rl.close();
  }
}).on("close", function () {
  solution(inputs);
  process.exit();
});
