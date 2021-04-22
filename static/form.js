$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				fileInput : $('#fileInput').val()
			},
			type : 'POST',
			url : '/'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});