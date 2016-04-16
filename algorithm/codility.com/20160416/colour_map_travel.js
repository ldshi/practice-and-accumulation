(function solution(A) {

  var divider = '^_^';

  var generate_guid = function() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  };

  var blazer = function(idx_x, idx_y) {
    var color_id = A[idx_x][idx_y];
    var area_id = '';

    if (isNaN(color_id)) {
      area_id = color_id;

      var tmp_str = color_id.toString();
      color_id = tmp_str.substring(0, tmp_str.indexOf(divider));
    } else {
      area_id = color_id + divider + generate_guid();
    }

    A[idx_x][idx_y] = area_id;

    tmp_up = idx_x - 1;
    while (tmp_up >= 0) {
      var tmp_color_id = A[tmp_up][idx_y];

      if (isNaN(tmp_color_id)) {
        var tmp_str = tmp_color_id.toString();
        tmp_color_id = tmp_str.substring(0, tmp_str.indexOf(divider));
      }

      if (tmp_color_id == color_id) {
        A[tmp_up][idx_y] = area_id;
        tmp_up--;
      } else {
        break;
      }
    }

    tmp_right = parseInt(idx_y) + 1;
    while (tmp_right < A[0].length) {
      var tmp_color_id = A[idx_x][tmp_right];

      if (isNaN(tmp_color_id)) {
        var tmp_str = tmp_color_id.toString();
        tmp_color_id = tmp_str.substring(0, tmp_str.indexOf(divider));
      }

      if (tmp_color_id == color_id) {
        A[idx_x][tmp_right] = area_id
        tmp_right++;
      } else {
        break;
      }
    }

    tmp_down = parseInt(idx_x) + 1;
    while (tmp_down < A.length) {
      var tmp_color_id = A[tmp_down][idx_y];

      if (isNaN(tmp_color_id)) {
        var tmp_str = tmp_color_id.toString();
        tmp_color_id = tmp_str.substring(0, tmp_str.indexOf(divider));
      }

      if (tmp_color_id == color_id) {
        A[tmp_down][idx_y] = area_id;
        tmp_down++;
      } else {
        break;
      }
    }

    tmp_left = idx_y - 1;
    while (tmp_left >= 0) {
      var tmp_color_id = A[idx_x][tmp_left];

      if (isNaN(tmp_color_id)) {
        var tmp_str = tmp_color_id.toString();
        tmp_color_id = tmp_str.substring(0, tmp_str.indexOf(divider));
      }

      if (tmp_color_id == color_id) {
        A[idx_x][tmp_left] = area_id;
        tmp_left--;
      } else {
        break;
      }
    }

  };

  var processer = function() {
    for (var idx in A) {
      for (var idx_inner in A[idx]) {
        blazer(idx, idx_inner);
      }
    }
  };

  var aggregater = function() {
    var res = {};
    
    for (var idx in A) {
      for (var idx_inner in A[idx]) {
        if (res[A[idx][idx_inner]]) {
          res[A[idx][idx_inner]]++;
        } else {
          res[A[idx][idx_inner]] = 1;
        }
      }
    }

    return Object.keys(res).length;
  };

  processer();

  console.log(aggregater());

})([
  [5, 4, 4],
  [4, 3, 4],
  [3, 2, 4],
  [2, 2, 2],
  [3, 3, 4],
  [1, 4, 4],
  [4, 1, 1]
]);


