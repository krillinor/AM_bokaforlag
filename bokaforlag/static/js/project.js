
////////////////////////////////////////////////////////////////////////////////
// uppfærir heildarverð í modal í pöntun
////////////////////////////////////////////////////////////////////////////////

const $sendapontun = $("#senda-pontun");
const $modalmagn = $("#modal-magn");
const $modalheildarverd = $("#modal-heildarverd");

$(() => {
  $sendapontun.on("click", () => {
    let verd = parseInt($("#verd").text());
    let magn = parseInt($("#id_magn").val());
    let heildarverd = verd * magn;
    $modalmagn.html(magn);
    $modalheildarverd.html(heildarverd);
  })
})

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
