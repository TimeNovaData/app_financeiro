function applyMasksItemFornecedorInline() {
  document
    .querySelector("#itemfornecedor_set-group .add-row a")
    .addEventListener("click", (event) => {
      // Máscara do telefone
      const telefoneInput = $("[id$='-telefone']");
      telefoneInput[0] && telefoneInput.mask("(00) 0 0000-0000");
    });
}
