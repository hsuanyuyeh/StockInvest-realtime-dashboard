$(document).ready(function(){
	var dataTable = $("#dataTable").DataTable()
	var customerChannel = pusher.subscribe('record');
	customerChannel.bind('add', function(data) {
	var date = new Date();
	dataTable.row.add([
	    data.stock_name,
	    `${date.getMonth()}/${date.getDay()}/${date.getFullYear()}`,
			data.buy_sell,
			data.price,
			data.amount,
			data.cost_reward
	  ]).draw( false );
	});
});