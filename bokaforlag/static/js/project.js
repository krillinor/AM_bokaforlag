
$(() => {
  //////////////////////////////////////////////////////////////////////////////
  // uppfærir heildarverð í modal í pöntun
  //////////////////////////////////////////////////////////////////////////////
  const $sendapontun = $("#senda-pontun");
  const $modalmagn = $("#modal-magn");
  const $modalheildarverd = $("#modal-heildarverd");

  $sendapontun.on("click", () => {
    let verd = parseInt($("#verd").text().replace(".", ""));
    let magn = parseInt($("#id_magn").val());
    let heildarverd = (verd * magn) / 1000;
    $modalmagn.html(magn);
    $modalheildarverd.html(heildarverd);
  })

  //////////////////////////////////////////////////////////////////////////////
  // hringekja
  //////////////////////////////////////////////////////////////////////////////
  let $hringekja = $('.hringekja'),
      $haegri = $('.forsidubok.haegri');
      interval = 5000;

  $hringekja.each(function() {
    $(this).owlCarousel({
        loop: true,
        margin: 10,
        items: 1,
        animateIn: 'fadeIn',
        animateOut: 'fadeOut',
        autoplay: true,
        autoplayTimeout: interval,
        autoplayHoverPause:true,
        dots: false
        // kiddi
        // mouseDrag: false,
        // touchDrag: false,
        // pullDrag: false,
        // freeDrag: false
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
  function resizeBok() {
    const $forsidubok = $(".forsidubok"),
          $bokamynd = $(".bokamynd").first();
          $lysing = $(".item-lysing");
    $forsidubok.each(function() {
      $(this).width($bokamynd.width());
    })
    $lysing.each(function() {
      $(this).width($bokamynd.width());
    })
  }

  resizeBok();
  $(window).resize(function() {
    resizeBok();
  })

})
