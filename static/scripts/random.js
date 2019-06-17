var states2;

jQuery.ajax({
        url:'http://10.5.33.255:5000/static/hgnc_gene_names_sorted.txt', 
        success: function(data) {
            states2 = data.split("\n");
        }, 
        async:false});

var substringMatcher = function(strs) {
    return function findMatches(q, cb) {
      var matches, substringRegex;
  
      // an array that will be populated with substring matches
      matches = [];
  
      // regex used to determine if a string contains the substring `q`
      substrRegex = new RegExp(q, 'i');

      // iterate through the pool of strings and for any string that
      // contains the substring `q`, add it to the `matches` array
      $.each(strs, function(i, str) {
        if (substrRegex.test(str)) {
          matches.push(str);
        }
      });
  
      cb(matches);
    };
};

 
  $('#my_search').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
  },
  {
    name: 'states2',
    source: substringMatcher(states2)
  });

