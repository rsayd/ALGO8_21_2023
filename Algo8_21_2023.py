
/* 
  Write a recursive function that, given a number,
  returns the sum of integers from one up to that
  number.
  
  For example,
  rSigma(5) = 1 + 2 + 3 + 4 + 5 = 15;
  rSigma(2.5) = 1 + 2 = 3;
  rSigma(-1) = 0.
*/

/* 
Requirements for Recursion
1. Base Case (exit clause - stops the loop)
2. Progression towards base case
3. Call function inside itself
*/

function sigma(num) {
  if (num <= 0) {
    return 0;
  }

  num = Math.floor(num);
  let sum = 0;

  for (let i = 1; i <= num; i++) {
    sum += i;
  }

  return sum;
}

/**
 *
 * @param {number} num
 * @returns {number}
 */
function rSigma(num) {
  if (num < 1) {
    return num;
  }

  num = Math.floor(num);

  return rSigma(num - 1) + num;
}

console.log(sigma(5));
console.log(rSigma(5));
[8:42 AM]
/* 
Recursive Factorial
Given a number `num`, return the product of integers from 1 upward to that number.
If less than or equal to zero, return -1. If not an integer, treat as an integer.

Input: integer
Output: product of integers from 1 to input integer
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1 * 2 * 3 = 6

const num2 = 5;
const expected2 = 120;
// Explanation: 1 * 2 * 3 * 4 * 5 = 120

const num3 = 3.5;
const expected3 = 6;
// Explanation: 1 * 2 * 3 = 6

const num4 = 0;
const expected4 = -1;
// Explanation: num is zero, return -1

const num5 = -1;
const expected5 = -1;
// Explanation: num is less than zero, return -1

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function rFactorial(num) {
  // pseudo code
  // base case
  // progression
  // call itself
}
[8:42 AM]
/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums) {
  //
}



Answer:

const num1 = 3;
const expected1 = 6;
// Explanation: 1 * 2 * 3 = 6

const num2 = 5;
const expected2 = 120;
// Explanation: 1 * 2 * 3 * 4 * 5 = 120

const num3 = 3.5;
const expected3 = 6;
// Explanation: 1 * 2 * 3 = 6

const num4 = 0;
const expected4 = -1;
// Explanation: num is zero, return -1

const num5 = -1;
const expected5 = -1;
// Explanation: num is less than zero, return -1

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function rFactorial(num) {
  // pseudo code
  num = Math.floor(num);
  if (num == 1) {
    return 1;
  }
  if (num <= 0) {
    return -1;
  }

  return rFactorial(num - 1) * num;

  // base case
  // progression
  // call itself
}

console.log(rFactorial(num1), "should be", expected1);
console.log(rFactorial(num2), "should be", expected2);
console.log(rFactorial(num3), "should be", expected3);
console.log(rFactorial(num4), "should be", expected4);
console.log(rFactorial(num5), "should be", expected5);
const nums6 = [1, 2, 3];
const expected6 = 6;

const nums7 = [1];
const expected7 = 1;

const nums8 = [];
const expected8 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums) {
  if (nums.length == 0) {
    return 0;
  }

  let x = nums.pop();

  return sumArr(nums) + x;
}
console.log("************************");
console.log(sumArr(nums6), "should be", expected6);
console.log(sumArr(nums7), "should be", expected7);
console.log(sumArr(nums8), "should be", expected8);

