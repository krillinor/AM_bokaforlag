
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
