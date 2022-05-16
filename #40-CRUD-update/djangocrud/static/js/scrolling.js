$(window).scroll(function () {
    const scroll = $(window).scrollTop();
    if (scroll >= 10) {
      $("#navIndex").addClass("bg-dark");
    } else {
      $("#navIndex").removeClass("bg-dark");
    }
  });
  