// frontend/src/components/Search/SearchBar.js
import React, { useState } from 'react';
import axios from 'axios';

function SearchBar({ setSearchResults }) {
  const [query, setQuery] = useState('');

  const handleSearch = async () => {
    const response = await axios.get(`http://127.0.0.1:5000/notes/search?query=${query}`);
    setSearchResults(response.data);
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search notes"
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
}

export default SearchBar;
