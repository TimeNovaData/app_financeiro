function applyMasksDadoBancario() {
  const agenciaInput = $("#id_agencia");
  agenciaInput[0] && agenciaInput.mask("0000");

  const contaInput = $("#id_conta");
  contaInput[0] && contaInput.mask("0000000-0");
}
