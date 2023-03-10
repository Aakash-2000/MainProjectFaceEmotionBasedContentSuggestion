const arr = [
  "apple",
  ,
  "orange",
  "mango",
  "banana",
  "mango",
  "apple",
  "orange",
  ,
  "grapes",
  ,
  "orange",
];
console.log(arr.length);
let ans = arr.reduce((acc, cur) => {
  // console.log(cur);
  if (acc[cur]) {
    acc[cur] += 1;
  } else {
    acc[cur] = 1;
  }
  return acc;
}, {});
console.log(ans);
