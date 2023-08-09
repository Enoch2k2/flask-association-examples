import React from 'react'

const ItemCard = ({ item, addItemToCart }) => {


  return (
    <li key={ item.id }>{ item.name } - <button onClick={ () => addItemToCart(item) }>Add To Cart</button></li>
  )
}

export default ItemCard