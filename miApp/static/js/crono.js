function giveVuelta() {

        var vuelta= document.getElementById("stopwatch").innerHTML;
        var capa = document.getElementById("capa");
        var h1 = document.createElement("h1");
        h1.innerHTML = vuelta;
        capa.appendChild(h1);
    }

    function resetear(){
        var boton = document.getElementById("botonPlay");
        if (boton.value=="Iniciar"){
            boton.setAttribute("value", 'Pausar');
        }
        else{
            boton.setAttribute("value", 'Iniciar');
        }
    }

    function borrar(){
        var capa = document.getElementById("capa");
        capa.innerHTML = "";

        var boton = document.getElementById("botonPlay");
        boton.setAttribute("value", 'Iniciar');
    }