$(document).ready(function(){           
// var cuotas = [];
// alertify.defaults.transition = "slide";
// alertify.defaults.theme.ok = "btn btn-primary";
// alertify.defaults.theme.cancel = "btn btn-danger";
// alertify.defaults.theme.input = "form-control";


// $("#checkall").click (function () {
//      var checkedStatus = this.checked;
//     $("input[class='tildado']").each(function () {
//         $(this).prop("checked", checkedStatus);
//         $(this).change();
//      });
//   });
 
  
//   $("input[class='tildado']").change(function() {      
//       checkBoxClick();               
//   });
    
  
//   function checkBoxClick() {
//     cuotas = [];
//     total = 0.00;
//     montoLiq = 0.00;

//     cant = 0; 
//     $("input[class='tildado']").each(function(index,checkbox){
//         if(checkbox.checked){               
//          idcta = document.getElementById(checkbox.id+"_id_cuota").value               
//          saldo = parseFloat(document.getElementById("saldo_"+checkbox.id).value.replace(/,/, '.'));
//          montoLiq = document.getElementById("total_"+checkbox.id)       ;
//          if (montoLiq) { saldo = parseFloat(montoLiq.value.replace(/,/, '.')); }         
//          cuotas.push(idcta);     
//          total += saldo;
//          cant += 1; 
         
//          $(checkbox).closest('tr').toggleClass('selected', checkbox.checked);
//     }
//     else {  
//         if($(checkbox).closest('tr').hasClass('selected')){
//           $(checkbox).closest('tr').removeClass('selected');}
//         }
//     });
//     $("#montoLiq").text(parseFloat(total).toFixed(2));
//     $("#montoLiqCant").text(cant);
// }

// $('#generarLiq').click(function(){
    
//     if (cuotas)
//     {
//       idp = document.getElementById("id_padron").value
//       datos = []
      
//       $.ajax({
//         url: "/punitoriosLiq/"+idp,
//         type: "get",
//         dataType: 'json',
//         data: {'cuotas[]': cuotas},
//         success: function(data) {
//             var $subtot = 0;
//             for(var key in data){
//               $subtot += parseFloat(data[key]);};
//             console.log(data);
//             $subtot = $subtot.toFixed(2);

//             var closable = alertify.dialog('confirm').setting('closable');
//             //grab the dialog instance and set multiple settings at once.
//             alerta= alertify.dialog('confirm')
//               .set({
//                 'labels':{ok:'Guardar e Imprimir', cancel:'Cancelar'},
//                 'message': 'El monto de la Liquidación (punitorios al día de la fecha) es de : $ '+ $subtot ,
//                 'onok': function(){ 
//                   datos = data;
//                   $.ajax({
//                     url: "/liquidacion/"+idp,
//                     type: "get",
//                     dataType: 'json',
//                     data: {'cuotas[]': cuotas},
//                     success: function(data) {
//                       // alertify.success('El monto a pagar es: $ '+ $subtot);
//                       url = "/imprimirLiqWeb/"+data;
//                       var win = window.open(url, '_blank');
                                            
//                       location.reload();
//                         }});                  
//                 },
//                 'oncancel': function(){ location.reload();}
//               });
//               alerta.setHeader('Liquidación OnLine');
//               alerta.show();
//         }});
//     } 
// });

});
