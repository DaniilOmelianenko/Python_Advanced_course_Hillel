const ws = new WebSocket('ws://' + window.location.host + '/ws');


ws.onmessage = function (event) {
    let bets_box = '<div class="alert alert-dark" role="alert">' + event.data + '</div>';
    $('.trade-window').append(bets_box);
};

$('#make_bet').click(function () {
    const my_bet_text = $('#my_bet_text').val();
    $('#my_bet_text').val('');
    ws.send(my_bet_text);
});

$('#add_lot-btn').click(function () {
    const lot_price = $('#lot_start_price').val();
    const lot_summary = $('#lot_summary').val();
    if (lot_summary && lot_price) {
        fetch('/create/lot', {
            method: 'POST',
            body: JSON.stringify({'name': lot_summary, 'price': lot_price}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(async function (res) {
            const data = await res.json;
            let lot_box = '<a href="/lot/'+data.id+'" class="alert alert-warning" role="alert">'+lot_summary+': '+lot_price+'</a>';
            $('#lot_list').append(lot_box);
            $('#lot_start_price').val('');
            $('#lot_summary').val('');
        });

    }
});