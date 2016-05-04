var BitTitan = BitTitan || {};

BitTitan.funcs = {
  calculate: function() {
    var trs = $('#repair-invoice').find('tr');
    var total = 0;

    $.each(trs, function(idx, val) {
      var tds = $(val).find('td');

      if (tds.length === 4) {
        var subtotal = 0;
        subtotal = parseFloat($(tds[1]).text()) + parseFloat($(tds[2]).text());
        $(tds[3]).text(subtotal.toFixed(2));

        total += subtotal;
      } else if (tds.length === 2) {
        $(tds[1]).text(total.toFixed(2));
      }
    });
  }
};

$(document).ready(function() {
  BitTitan.funcs.calculate();
});


