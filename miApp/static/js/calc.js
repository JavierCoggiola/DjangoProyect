resetear = false;

        function suma(var1, var2) {
            return var1+var2;   
        }

        function ejecutar(boton) {
            aprieta = boton.value;


            if (resetear==true){
                document.getElementById("operaciones").setAttribute("value", "");
                resetear = false;
            }

            val = document.getElementById("operaciones").value;

            if (aprieta=="="){
                resetear = true;
                if (val.length!=0){ // para q no de error.
                    result = eval(val);//TODO Hacer la funcion que me de el resultado
                    //eval resuelve todo.
                    document.getElementById("operaciones").setAttribute("value", result);
                }

            }
            else if(aprieta=="CLEAR"){
                document.getElementById("operaciones").setAttribute("value", "");
                //document.getElementById("operaciones").value("");
            }
            else{ 
                document.getElementById("operaciones").setAttribute("value",val+aprieta);
                //concatenando texto en el cuadro.
            }            

        }