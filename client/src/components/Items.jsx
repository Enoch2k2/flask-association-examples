import React from 'react'
import ItemCard from './ItemCard'

const Items = ({ addItemToCart }) => {
  const items = [
    {
      id: 1,
      name: "Pizza"
    },
    {
      id: 2,
      name: "Salad"
    },
    {
      id: 3,
      name: "Milk Shake"
    }
  ]

  const itemCards = items.map(item => <ItemCard key={ item.id } item={ item } addItemToCart={ addItemToCart } />)

  return (
    <ul>
      { itemCards }
    </ul>
  )
}

export default Items