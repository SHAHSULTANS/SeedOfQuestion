let name = "shanto";
console.log(name);

//genral function:

function add(a, b) {
  console.log(this);
  return a + b;
}

// console.log(add(2,6));

ob = {
  age: "24",
  value: add(2, 4),
};
console.log(ob.value);

//arrow function

const summarizer = (name, age) => {
  console.log(this);
  return `Hi I am ${name}. I am ${age} years old `;
};

console.log(summarizer(name, "25"));

//map function js

const numbers = [1, 2, 3, 4];
const doub = numbers.map((num) => {
  return num * 2;
});
console.log(doub);

//callback function

function multipley(a, b, callback) {
  res = a * b;
  callback(res);
}

function result(res) {
  console.log(res);
}

multipley(4, 5, result);
//same result callback function.
multipley(4, 5, function (res) {
  console.log(res);
});

//spread opreator reutrn new array. Don't modify orginal array
let nums = [1, 2, 3];

let more = [...nums, 4, 5];
console.log(more);

//rest opreator. all paratemeter takes one array.

function sum(...arg) {
  //exceute some
}
sum(1, 2, 5); //we can pass any number of argument

///destructuring
//array
const [first, second, ...rest] = nums;
console.log(first, second);
console.log(rest);

///object destructuring

person = {
  username: "shanto",
  age: 24,
  roll: 379,
};

const { username, roll, ...otherinfo } = person;

// console.log(username);
// console.log(otherinfo);
// console.log("shanto");

console.table(nums);
