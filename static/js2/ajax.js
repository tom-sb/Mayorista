$(document).ready(function() {
	$("#search-proveedor").submit(function(e){
		e.preventDefault();

		$.ajax({
			url: $(this).attr('action'),
			type: $(this).attr('method'),
			data: $(this).serialize(),

			success: function(json){
				console.log(json)
				var html = ""
				
				for (var i=0; i<json.length; i++){
				html += '<tr><td>'+json[i].id+ '</td><td>'+
					json[i].nombreEmpresa+ '</td><td>'+
					json[i].nombreRepresentante+'</td></tr>'
				 
				}
				$("#datosC").html(html);
			}
		})
	})


})