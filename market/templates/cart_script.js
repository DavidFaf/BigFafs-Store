let add_to_cart_btns = document.getElementsByClassName('btn-success')

for(let i=0; i<add_to_cart_btns.length; i++){
    add_to_cart_btns[i].addEventListener('click', addToCart)
}


function addToCart(event){
    '{% for item in items %}'
    let btn = event.target

    let item_name= '{{item.name}}'
    let item_price = '{{item.price}}'
    let item_image = document.getElementsByClassName('card-img-top')

    console.log(item_name)
    console.log(item_price)

    '{% endfor %}'
}


