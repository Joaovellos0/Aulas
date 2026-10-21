/**
 * MÙSIC Shop - JavaScript da Página de Cadastro
 * Formatação e máscara de campos
 */

document.addEventListener('DOMContentLoaded', function () {
    const telInput = document.getElementById('cad_telefone');
    if (telInput) {
        telInput.addEventListener('input', function (e) {
            // Apenas dígitos
            this.value = this.value.replace(/\D/g, '').slice(0, 9);
        });
    }
});
