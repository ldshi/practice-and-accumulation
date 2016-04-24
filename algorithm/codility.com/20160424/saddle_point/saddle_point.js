function solution(A) {

  var rows = A.length;
  var cols = A[0].length;
  var i = 0;
  var j = 0;

  var is_local_max = function (i, nums) {
    nums = nums || [];
    if (i > 0 && i < nums.length - 1) {
      return nums[i] > nums[i - 1] && nums[i] > nums[i + 1];
    }
    return false;
  };

  var is_local_min = function (num, nums) {
    nums = nums || [];
    if (i > 0 && i < nums.length - 1) {
      return nums[i] < nums[i - 1] && nums[i] < nums[i + 1];
    }
    return false;
  };

  var matrix_displace = function (matrix) {
    var result = [];
    var rows = matrix.length;
    var cols = matrix[0].length;

    for (var i = 0; i < rows; i++) {
      for (var j = 0; j < cols; j++) {
        result[j] = result[j] || [];
        result[j][i] = result[j][i] || [];
        result[j][i] = matrix[i][j];
      }
    }

    return result;
  };

  var matrix = matrix_displace(A);
  var count = 0;

  for (; i < rows; i++) {
    for (j = 0; j < cols; j++) {
      if (is_local_min(j, A[i]) && is_local_max(i, matrix[j])) {
        count++;
      } else if (is_local_max(j, A[i]) && is_local_min(i, matrix[j])) {
        count++;
      }
    }
  }

  return count;
};


