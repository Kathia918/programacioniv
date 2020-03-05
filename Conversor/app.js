document.addEventListener("DOMContentLoaded",e=>{
    document.addEventListener("submit",event=>{
        event.preventDefault();

        let de = document.querySelector("#cboDe").value,
            a = document.querySelector("#cboA").value,
            cantidad = document.querySelector("#txtCantidadConversores").value,
            $res = document.querySelector("#lblRespuestaPeso");
        let Peso={
            'Libra':1,
            'gramo':453.592,
            'onza':16,
            'Kilogramo':0.453592,
            'miligramo':453592
        };
        $res.innerHTML = `Respuesta: ${ Peso[a] / Peso[de] * cantidad }`;
    });
});