/*
 * Specific to platform 'www.codeforces.com'.
 */

var amount = 0, counter = 1;
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

amount = parseInt(readline())

while (1) {
  var line = readline();
  if (line) {
    accumulator(counter, line.trim().split(' '));
  } else {
    break;
  }

  counter++;
}



print(accumulation.length);
for (var idx in accumulation) {
  var item = accumulation[idx];
  print(item[0].length + ' ' + item[0].join(' '));
}


