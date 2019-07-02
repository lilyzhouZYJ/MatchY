<<<<<<< HEAD
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
=======
function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;
    
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";

  }
>>>>>>> 62f8a435b7cefe3a15277dea784a9323c28c2531
