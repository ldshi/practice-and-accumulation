function solution(E, L) {
  var fee_entr = 2;
  var fee_1st_h = 3;
  var fee_after_2nd_per_h = 4;

  var e_arr = E.split(':');
  var l_arr = L.split(':');

  var in_min = (parseInt(l_arr[0]) - parseInt(e_arr[0])) * 60 - parseInt(e_arr[1]) + parseInt(l_arr[1]);

  if (in_min <= 60) {
    return (fee_entr + fee_1st_h);
  } else {
    if (in_min % 60 === 0) {
      return (fee_entr + fee_1st_h + (in_min / 60 - 1) * fee_after_2nd_per_h);
    } else {
      return (fee_entr + fee_1st_h + (parseInt(in_min / 60)) * fee_after_2nd_per_h);
    }
  }
}


