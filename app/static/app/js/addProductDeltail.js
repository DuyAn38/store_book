var updateBtns = document.getElementsByClassName('addProductDeltail')
for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var quantityInputValue = document.querySelector('.quantity-input').value;
        console.log("id sản phẩm: ", productId);
        console.log('action: ', action);
        console.log('user: ', user)
        console.log('so luong: ', quantityInputValue)

        if (user === "AnonymousUser") {
            console.log("User not login");
        } else {
            updateUserOrder(productId, action, quantityInputValue);
        }
    })
}

function updateUserOrder(productId, action, quantityInputValue ){
    console.log("User login ok");
    console.log("id: ", productId);
    console.log("action 2: ", action);
    console.log("so luong: ", quantityInputValue);
    var url = '/updateItem/';
    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action, 'count': quantityInputValue})
    }).then((reponse) =>{
       return reponse.json();
       
    }).then((data) =>{
        console.log('data: ', data)
        location.reload();
    })
}
