

$(document).ready(function() {

	$(".editable-text").each(function ()
	{
		$(this).click( function(event) {
		    $(this).next().show("fast");
		    $(this).hide("fast");

		});
	});

	$(".btn.btn-cancel").each(function()
		{
			$(this).click(function(event){
				$(this).parents(".edit-text").hide("fast");
				$(this).parents(".edit-text").prev().show("fast");
			});
		});

});