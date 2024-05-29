// frontend/src/components/Auth/Logout.js
import React from 'react';
import axios from 'axios';

function Logout({ setAuth }) {
  const handleLogout = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/auth/logout');
      alert(response.data.message);
      setAuth(false); // Set the auth state to false on successful logout
    } catch (error) {
      alert('Error logging out');
    }
  };

  return <button onClick={handleLogout}>Logout</button>;
}

export default Logout;
