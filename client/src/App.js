import { useEffect, useState } from "react";
import Home from "./components/Home";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from "./components/Navbar";
import UserList from "./components/users/UserList";
import UserForm from "./components/users/UserForm";
import Errors from "./components/Errors";

const App = () => {
  const [users, setUsers] = useState([])
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/users')
      .then(resp => resp.json())
      .then(data => setUsers(data))
  }, [])

  const addUser = data => {
    if(data.error) {
      setError(data.error);
    } else {
      setUsers([...users, data])
    }
  }

  return (
    <div className="App">
      <BrowserRouter>
        <Navbar />
        <Errors error={error} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<UserList users={ users } />} />
          <Route path="/users/new" element={<UserForm addUser={ addUser } setError={setError} />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
