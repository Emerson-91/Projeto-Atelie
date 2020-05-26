function Alerta(){

alert("Se não faltou algum campo obrigatorio Salvou");
}

function Fechar(){
style.display = 'none';
}
$(document).ready(function()){
    var ShowForm = function(){
    vat btn = $(this);
    $.ajax({
    url: btn.attr("data-url")
    })


}}