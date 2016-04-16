(function solution(A) {
  
  if (!A) {
    console.log(0);
    return;
  }

  if (A.length < boundary_1_7_type) {
    console.log(A.length * type_1_day_ticket);
    return;
  }

  var type_1_day_ticket = 2;
  var type_7_day_ticket = 7;
  var type_30_day_ticket = 30;

  var boundary_1_7_type = 4;

  var total_cost = 0;
  var begin = 0;
  var end = 0;

  while (A.length >= boundary_1_7_type) {
    end = begin + 3;

    while (end < A.length && A[end] - A[begin] < type_7_day_ticket) {
      end++;
    }

    if (end > 3) {
      total_cost += type_7_day_ticket

      A = A.slice(end, A.length);
    } else {
      total_cost += type_1_day_ticket;

      A = A.slice(begin + 1, A.length);
    }

    begin = end = 0;
  }

  total_cost += A.length * type_1_day_ticket;

  if (total_cost > type_30_day_ticket) {
    console.log(type_30_day_ticket);
  } else {
    console.log(total_cost);
  }

})([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,24, 25, 26, 27, 28, 29, 30]);


