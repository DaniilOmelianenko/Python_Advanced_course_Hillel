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