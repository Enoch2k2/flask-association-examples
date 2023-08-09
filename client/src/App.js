import { useEffect, useState } from "react";
import Items from "./components/Items";
import Cart from "./components/Cart";

const App = () => {

  const [cart, setCart] = useState([])

  useEffect(() => {
    const storedCart = localStorage.getItem('cart')
    if (storedCart) {
      const parsedCart = JSON.parse(storedCart);
      setCart(parsedCart)
    } else {
      localStorage.setItem('cart', JSON.stringify(cart))
    }
  }, [])

  const updateCart = updatedCart => {
    setCart(updatedCart)
    localStorage.setItem('cart', JSON.stringify(updatedCart))
  }

  const addItemToCart = (item) => {
    // store the item to localStorage
    updateCart([...cart, item])
  }

  const checkout = () => {
    cart.reduce((a, b)  => a + b.price, 0)

    updateCart([])
  }

  return (
    <div className="App">
      <Cart cart={ cart } />
      <Items addItemToCart={ addItemToCart } />
      <button onClick={ checkout }>Check Out!</button>
    </div>
  );
}

export default App;
