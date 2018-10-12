/* Project specific Javascript goes here. */

// header nav
// const headernav = $("#header-nav");
// const headernavlink = $("#header-nav .nav-link");
//
// $(document).ready(function() {
//   headernavlink.on("click", function (e) {
//     headernav.find(".nav-link").removeClass("active");
//     $(this).addClass("active");
//     // alert("virkar");
//   })
// });

// hringekja
let $hringekja = $('.hringekja'),
    $haegri = $('.forsidubok.haegri');
    interval = 5000;

$hringekja.each(function() {
  $(this).owlCarousel({
      loop:true,
      margin:10,
      items: 1,
      animateIn: 'fadeIn',
      animateOut: 'fadeOut',
      autoplay: true,
      autoplayTimeout: interval,
      autoplayHoverPause:true,
      dots: false
    });
});

let $owl = $hringekja.last();
let autoplayDelay = 2000;

if (autoplayDelay) {
   $owl.trigger('stop.owl.autoplay');
   setTimeout(function() {
    $owl.trigger('play.owl.autoplay');
   }, autoplayDelay);
}
