import React from 'react'

const Cart = ({ cart }) => {
  return (
    <ul>
      { cart.map((item, idx) => <li key={ idx }>{ item.name } </li>)}
    </ul>
  )
}

export default Cart