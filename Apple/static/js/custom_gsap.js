
$(document).ready(function () {
  $(".item").mouseenter(function () { 
    // $('.remove').css("display",'block');
    $('.remove').fadeIn('slow');

  });
  $(".item").mouseleave(function () { 
    // $('.remove').css("display",'none');
    $('.remove').fadeOut('slow');


  });
});

