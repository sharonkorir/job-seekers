//modal jquery

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems, options);
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, options);
});

// Or with jQuery

$(document).ready(function(){
  $('.modal').modal();
  $('.sidenav').sidenav();
});

