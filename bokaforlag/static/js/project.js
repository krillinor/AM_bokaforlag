
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

  if ($hringekja.length > 0) {
    $hringekja.each(function() {
      $(this).owlCarousel({
          loop: true,
          margin: 10,
          items: 1,
          animateIn: 'fadeIn',
          animateOut: 'fadeOut',
          autoplay: true,
          autoplayTimeout: interval,
          autoplayHoverPause: true,
          dots: false,
          // kiddi
          mouseDrag: false,
          touchDrag: false,
          pullDrag: false,
          freeDrag: false
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

    let forsidubok = $(".hringekja"),
        bokamynd = $(".bokamynd").first(),
        lysing = $(".item-lysing");

    function resizeBok() {
      forsidubok = $(".hringekja"),
      bokamynd = $(".bokamynd").first(),
      lysing = $(".item-lysing");
      forsidubok.each(function() {
        $(this).width(bokamynd.width());
      })
      lysing.each(function() {
        $(this).width(bokamynd.width());
      })
    }

    $(window).resize(function() {
      resizeBok();
    })

    bokamynd.on('load', function() {
      resizeBok();
    });

    // bara til að tryggja að containerinn verði jafn stór og myndin
    let t = setTimeout(function() {
      if (bokamynd.width() < 100)
        return; // keyrum aftur
      else {
        resizeBok();
        forsidubok.first().addClass("forsidubok vinstri");
        forsidubok.last().addClass("forsidubok haegri");
        clearTimeout(t);
      }
    }, 10)

  }

  // kennitöludót, setja bandstrik ef 10 tölustafir
  const $kt = $('#id_kennitala');
  if ($kt.length > 0) {
    $kt.focusout(function() {
      const val = $kt.val(),
            isnum = /^\d+$/.test(val);
      if (isnum && val.length == 10) {
        const newVal = val.substring(0, 6) + '-' + val.substring(6, 10);
        $kt.val(newVal);
      }
    })
  }

  // setja Ísland sem default land:
  $('#id_land').val('Ísland');


  // myndahringekja
  if ($("#myndahringekja").length > 0) {
    $("#myndahringekja").owlCarousel({
      loop: true,
      items: 1,
      animateIn: 'fadeIn',
      animateOut: 'fadeOut',
      autoplay: true,
      autoplayTimeout: 5000,
      dots: false,
      // kiddi
      mouseDrag: false,
      touchDrag: false,
      pullDrag: false,
      freeDrag: false
    });
  }

  let autoplayDelay2 = 2500;

  if (autoplayDelay2) {
     $("#myndahringekja").trigger('stop.owl.autoplay');
     const t = setTimeout(function() {
      $("#myndahringekja").trigger('play.owl.autoplay');
      clearTimeout(t);
     }, autoplayDelay2);
  }

});
