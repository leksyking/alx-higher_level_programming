#!/usr/bin/node
let i;
let j;
const square = Number(process.argv[2]);
if (!square) {
  console.log('Missing size');
} else {
  for (i = 0; i < square; i++) {
    for (j = 0; j < square; j++) {
      console.log('x');
    }
    console.log('');
  }
}
