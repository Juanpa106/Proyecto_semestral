function carro(codigo){
    Swal.fire({
        icon: 'warning',
        title: 'Encontraste Todo Lo que necesitas?',
        text: "No se podran revertir los cambios!",
        showCancelButton: true,
        cancelButtonColor: '#d33',
        confirmButtonText: "Si!",
        cancelButtonText: "Seguir Comprando"
      }).then((result) => {
        if (result.value) {
          Swal.fire(
            'Gracias!',
            'Vuelva Pronto',
            'success'
          ).then(function(){
              window.location.href = '/compra' + '.html/';
          })
        }
      })




}