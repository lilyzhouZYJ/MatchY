function openTab(tabName) {
  var tabcontent = document.getElementById(tabName);
  var tablink = document.getElementById(tabName.replace("-tab","-link"));
     
  if(tablink.checked){
        tabcontent.className += " active";
  }
  else{
        tabcontent.className = tabcontent.className.replace(" active","");
        var children = tabcontent.children;
        for(var i = 0; i<children.length; i++){
              var child = children[i];
              if(child.type=="text"){
                    child.value="";
              }
              else if(child.type=="select-one"){
                    var options = child.children;
                    child.value = options[0].value;
              }             
        }
  }
}
