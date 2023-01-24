function applyMasksFornecedor() {
  const cnpjInput = $("#id_cnpj");
  cnpjInput[0] && cnpjInput.mask("00.000.000/0000-00");

  const telefoneInput = $("#id_telefone");
  telefoneInput[0] && telefoneInput.mask("(00) 0 0000-0000");
}
