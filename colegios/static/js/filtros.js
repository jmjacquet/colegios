$(document).ready(function() {  

    $(".filtros a").click(function(){
        var obj = $(this);
        $(obj).closest(".btn-group").find(".btn").text($(obj).text() );
        $(obj).closest(".btn-group").find(".btn").val($(obj).attr("val"))
    });

    $('#menuanio').click(function(){

        var anio = $("#anio").val();
        var id_persona = $("#id_persona").val();

        var url = "/cuotas/"+id_persona+"/"+anio;
        $(location).attr('href',url);
    });
    

   

});

