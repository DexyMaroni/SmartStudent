// frontend/src/components/Notes/NoteEditor.js
import React, { useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import axios from 'axios';
import TagInput from './TagInput';

function NoteEditor({ note, onSave }) {
  const [content, setContent] = useState(note ? note.content : '');
  const [tags, setTags] = useState(note ? note.tags : []);

  const handleSave = async () => {
    const newNote = { content, tags };
    if (note) {
      await axios.put(`http://127.0.0.1:5000/notes/${note.id}`, newNote);
    } else {
      await axios.post('http://127.0.0.1:5000/notes', newNote);
    }
    onSave();
  };

  return (
    <div>
      <ReactQuill value={content} onChange={setContent} />
      <TagInput tags={tags} setTags={setTags} />
      <button onClick={handleSave}>Save</button>
    </div>
  );
}

export default NoteEditor;
