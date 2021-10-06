function encontrarProducto(){
    var busqueda = document.getElementById("buscar_bebida").value;
    var losProductos = document.querySelectorAll(".contenedor_producto")
    let categoriasMenu = document.querySelectorAll(".categorias")
    for (var i=0;i<losProductos.length;i++){
        losProductos[i].classList.remove("filtro_Producto")
        var NombrDelProducto = losProductos[i].firstElementChild.getElementsByTagName("p")[0].textContent;
        var Encontrado = NombrDelProducto.indexOf(busqueda)
        if (Encontrado==-1){
            losProductos[i].classList.add("filtro_Producto")
        }
    }
}

function seleccionarCategoria(){
    document.getElementById("buscar_bebida").value=""
    var losProductos = document.querySelectorAll(".contenedor_producto")
    for (var i=0;i<losProductos.length;i++){
        losProductos[i].classList.remove("filtro_Producto")
    }
    let categorias = document.querySelector('.menu_categories');
    let categoriaSeleccionada= categorias.value;
    let categoriasMenu = document.querySelectorAll(".categorias")
    for(var i = 0; i<categoriasMenu.length;i++){
        categoriasMenu[i].classList.remove("filtro_Categoria")
        let categoria = categoriasMenu[i].getElementsByTagName("h2")[0].textContent
        if(categoriaSeleccionada != "All"){
            if (categoriaSeleccionada != categoria){
                categoriasMenu[i].classList.add("filtro_Categoria")
            }
        }
    }
}