function CambiaPosicion(){
                        document.getElementById("Boton").style.marginTop=Math.floor(Math.random() * (250 + 1) + 0)+"px";
                        document.getElementById("Boton").style.marginLeft=Math.floor(Math.random() * (500 + 1) + 0)+"px";
                        a = document.getElementById("View");
                        a.value="Troleado";
                    }