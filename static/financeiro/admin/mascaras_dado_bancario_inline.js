function applyMasksDadoBancarioInline() {
  const btnFK = document.querySelector("#dadobancario_set-group .add-row a");
  btnFK && btnFK.addEventListener("click", applyMasks);

  function applyMasks() {
    const agenciaInput = $("[id$='-agencia']");
    agenciaInput[0] && agenciaInput.mask("0000");

    const contaInput = $("[id$='-conta']");
    contaInput[0] && contaInput.mask("0000000-0");
  }
  applyMasks();
}
