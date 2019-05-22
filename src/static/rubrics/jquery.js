
var new_entry_markup = function(){
	markup = "<td>" +
						'<div class="editable-text"> Añadir Entrada</div>' + 
						'<div class="edit-text" style="display: none;">' + 
							'<div class="w3-content">' +
							'<textarea name="text" cols="40" rows="10" maxlength="50" required="" id="id_text">Añadir Entrada</textarea> </div>' +
							'<div class="w3-row">' +
								'<div class="w3-half"> <button type="button" class="btn btn-accept"><i class="fas fa-check"> </i></button> </div>' +
								'<div class="w3-half"> <button type="button" class="btn btn-cancel"><i class="fas fa-times"></i></button> </div>' +
							'</div>' +
						'</div>' +
					'</td>';
	return markup;
}

var init_buttons = function(){

	$("textarea").focusout( function(event) {
		if($(".btn:hover").length)
			return;
		$(this).parents(".edit-text").hide("fast");
		$(this).parents(".edit-text").prev().show("fast");

	});

	$(".editable-text").each(function ()
	{
		$(this).unbind('click');
		$(this).click( function(event) {
		    $(this).hide("fast");
		    $(this).next().show("fast");
		    $(this).next().find("textarea").focus();
		});
	});


	$(".btn.btn-cancel").each(function()
		{

			$(this).unbind('click');
			$(this).click(function(event){
				$(this).parents(".edit-text").hide("fast");
				$(this).parents(".edit-text").prev().show("fast");
			});
		});

	$(".btn.btn-accept").each(function()
		{
			$(this).unbind('click');
			$(this).click(function(event){
				var current_val = $(this).parents(".edit-text").find("textarea").val();
				if(typeof(current_val)=="undefined") // Es numerico
					current_val = $(this).parents(".edit-text").find("input").val();
				$(this).parents(".edit-text").prev().text(current_val);

				$(this).parents(".edit-text").hide("fast");
				$(this).parents(".edit-text").prev().show("fast");
			});
		});

	$(".btn.btn-add-col").each(function()
		{
			$(this).unbind('click');
			$(this).click(function(event){
				var ncols = $('table').find('th').length - 1;
				var nrows = $('table').find("tr").length - 1;
				console.log($('table').find('tr'))
				console.log(nrows)
				console.log(ncols)

				$('table').find('tr').each(function(index)
				{
					markup = "";
					if(index==0) // Header
						markup += "<th>"+
			        	'<div class="editable-text" style=""> 0 </div>' +
			        	'<div class="edit-text" style="display: none;">' +
			        	'	<div class="w3-content"><input type="number" name="nlogro" value="0" step="any" required="" id="id_nlogro"> </div>' +
			        	'	<div class="w3-row">' +
			        	'		<div class="w3-half"> <button type="button" class="btn btn-accept"><i class="fas fa-check"> </i></button> </div>' +
			        	'		<div class="w3-half"> <button type="button" class="btn btn-cancel"><i class="fas fa-times"></i></button> </div>' +
			        	'	</div>' +
			        	'</div> ' +
		        	 	"</th>";
		        	else if(index==nrows)
		        		markup += '<td><button type="button" class="btn btn-del-col"><i class="fas fa-trash-alt"></i></button> </td>'
		        	else
		        		markup += new_entry_markup()


					var $last_entry = $(this).children().eq(ncols);
					$last_entry.before(markup);

					console.log($(this).children())
					init_buttons()
				});
			});
		});

	$(".btn.btn-add-row").each(function()
		{
			$(this).unbind('click');
			$(this).click(function(event){

				var ncols = $('table').find('th').length - 1;

				var markup = "<tr>";
				for(var i = 0; i<ncols; i++)
					markup += new_entry_markup();

				markup+='<td><button type="button" class="btn btn-del-row""><i class="fas fa-trash-alt"></i></button> </td>' +
						'</tr>';
				$('#table-rows').append(markup);
				init_buttons()
			});
		});

	$(".btn.btn-del-col").each(function()
		{
			$(this).unbind('click');
			$(this).click(function(event){
				var $td = $(this).closest("td");
				var index = $td.index();
				$('table').find('tr').each(function()
				{
					$(this).children().eq(index).remove()
				});
			});
		});

	$(".btn.btn-del-row").each(function()
		{
			$(this).unbind('click');
			$(this).click(function(event){
				$(this).parents("tr").remove()
			});
		});



}

$(document).ready(function() {
	init_buttons()

	$("#delete-rubric").click(function(){
	    var alertdiv =$('<h3> ¿Estas seguro de querer borrar esta rubrica?</h3>').appendTo($('.w3-main'))
	    alertdiv.dialog({
	            dialogClass: "no-close",
	    		within: ".w3-main",
	            width:650, height:150,
	            modal:true,
	            resizable: false, 
	            show: { effect: 'drop', direction: "left" }, 
	            hide: { effect:'drop', direction: "left"},

	            buttons: {
	                Confirmar: function() {
	                      $("#delete-form").submit()},
	                Cancelar: function() {
	                	$('#alertblanket').hide(0);
	                    $(this).dialog( "close" );}
	                }
	           });

	});
});