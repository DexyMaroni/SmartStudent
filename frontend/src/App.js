// frontend/src/App.js
import React, { useState } from 'react';
import './App.css';
import NoteList from './components/Notes/NoteList';
import EventList from './components/Events/EventList';
import Register from './components/Auth/Register';
import Login from './components/Auth/Login';
import Logout from './components/Auth/Logout';
import SearchBar from './components/Search/SearchBar';
import SearchResult from './components/Search/SearchResult';


function App() {
  const [isAuth, setIsAuth] = useState(false);
  const [searchResults, setSearchResults] = useState([]);

  return (
    <div className="App">
      <h1>Smart Student</h1>
      {isAuth ? (
        <>
          <Logout setAuth={setIsAuth} />
          <SearchBar setSearchResults={setSearchResults} />
          <SearchResult results={searchResults} />
          <NoteList />
          <EventList />
        </>
      ) : (
        <>
          <Register />
          <Login setAuth={setIsAuth} />
        </>
      )}
    </div>
  );
}

export default App;
