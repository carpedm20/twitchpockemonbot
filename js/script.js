
var users = [];
var keys= [];

var timer = setInterval(function() {
    if (users.length !=0) {
        GameBoyKeyDown(keys[0]);
        setTimeout(ku, 500);
    }
}, 500);

function kd(user, key) {
    users.push(user);
    keys.push(key);

    if (key == 'up')
        ko_key = '위'
    else if (key == 'down')
        ko_key = '아래'
    else if (key == 'left')
        ko_key = '왼쪽'
    else if (key == 'right')
        ko_key = '오른쪽'
    else 
        ko_key = key
    $('#inputs tr:last').after('<tr><td>'+user+'</td><td>'+ko_key+'</td></tr>'); 
}

function ku() {
    GameBoyKeyUp(keys[0]);
    $('#inputs tr:nth-child(3)').remove()
    keys.shift();
    users.shift();
}
