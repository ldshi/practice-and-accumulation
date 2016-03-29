/*
 * node --version -> v4.2.1
 */

var readline = require('readline');

var counter = amount = 0;
var accumulation = [];

function accumulator(road_number, road) {
  if (accumulation.length == 0) {
    accumulation[0] = [[road_number], road];
    return;
  }

  for (var idx in accumulation) {
    var item = accumulation[idx];
    if (item[1].indexOf(road[0]) == -1 && item[1].indexOf(road[1]) == -1) {
      item[0].push(road_number);
      item[1] = item[1].concat(road);
      return;
    }
  }

  accumulation.push([[road_number], road]);
}

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', function(line) {
  if (counter == 0) {
    amount = parseInt(line);
  } else {
    accumulator(counter, line.trim().split(' '));
  }

  counter++;
  
  if (counter >= amount) {
    rl.close();

    console.log(accumulation.length);
    for (var idx in accumulation) {
      var item = accumulation[idx];
      console.log(item[0].length + ' ' + item[0].join(' '));
    }
  }
});


