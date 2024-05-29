// frontend/src/components/Notes/NoteForm.js
import React, { useState } from 'react';
import TagInput from './TagInput';

function NoteForm() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [tags, setTags] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const note = { title, content, tags };
    console.log(note); // Send this note to the backend
    setTitle('');
    setContent('');
    setTags([]);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Title:</label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </div>
      <div>
        <label>Content:</label>
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
      </div>
      <TagInput tags={tags} setTags={setTags} />
      <button type="submit">Create Note</button>
    </form>
  );
}

export default NoteForm;
