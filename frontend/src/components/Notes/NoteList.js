// frontend/src/components/Notes/NoteList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function NoteList() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/notes')
      .then(response => {
        setNotes(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the notes!', error);
      });
  }, []);

  return (
    <div>
      <h2>Notes</h2>
      <ul>
        {notes.map(note => (
          <li key={note.id}>{note.content}</li>
        ))}
      </ul>
    </div>
  );
}

export default NoteList;
