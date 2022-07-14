function borrar(codigo){
    Swal.fire({
        icon: 'warning',
        title: 'Estas seguro?',
        text: "No se podran revertir los cambios!",
        showCancelButton: true,
        cancelButtonColor: '#d33',
        confirmButtonText: "Si, Eliminar!",
        cancelButtonText: "Cancelar"
      }).then((result) => {
        if (result.value) {
          Swal.fire(
            'Datos Borrados!',
            'Datos Borrados Correctamente',
            'success'
          ).then(function(){
              window.location.href = "/eliminar_producto/"+ codigo  ;
          })
        }
      })




}