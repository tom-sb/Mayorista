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
					html += '<ul></li>'+json[i].nombreEmpresa+'</li><li>'+json[i].nombreRepresentante+'</li></lu>'
				}
				$("#datos").html(html);
			}
		})
	})


})