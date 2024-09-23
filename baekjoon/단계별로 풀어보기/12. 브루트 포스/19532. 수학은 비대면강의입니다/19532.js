function solution(inputs) {
  const splits = inputs.split(" ");
  const [a, b, c, d, e, f] = splits;
  let x, y;
  if (a == 0) {
    y = c / b;
    x = (f - e * y) / d;
  } else if (b == 0) {
    x = c / a;
    y = (f - d * x) / e;
  } else if (d == 0) {
    y = f / e;
    x = (c - b * y) / a;
  } else if (e == 0) {
    x = f / d;
    y = (c - a * x) / b;
  } else {
    y = c * d - f * a != 0 ? (c * d - f * a) / (b * d - e * a) : 0;
    x = c - b * y != 0 ? (c - b * y) / a : 0;
  }

  console.log(x + " " + y);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  solution(line);
  rl.close();
}).on("close", function () {
  process.exit();
});
