var states;

jQuery.ajax({
        url:'http://10.5.33.255:5000/static/hgnc_gene_names_sorted.txt', 
        success: function(data) {
            states = data.split("\n");
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
  
  $('#gene').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
  },
  {
    name: 'states',
    source: substringMatcher(states)
  });



//phenotype

var phenotypeSuggest = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  remote: {
    url: '/test?query=%QUERY',
    wildcard: '%QUERY'
  }
});

$('#phenotype').typeahead({
  hint: true,
  highlight: true,
  minLength: 3
},
{
  name: 'phenotypes',
  display: 'value',
  source: phenotypeSuggest
});