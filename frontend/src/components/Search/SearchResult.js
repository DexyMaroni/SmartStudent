// frontend/src/components/Search/SearchResult.js
import React from 'react';

function SearchResult({ results }) {
  return (
    <div>
      {results.map((result) => (
        <div key={result.id}>
          <h3>{result.title}</h3>
          <div dangerouslySetInnerHTML={{ __html: result.content }} />
        </div>
      ))}
    </div>
  );
}

export default SearchResult;
