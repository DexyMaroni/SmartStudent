// frontend/src/components/Notes/TagInput.js
import React, { useState } from 'react';

function TagInput({ tags, setTags }) {
  const [tagInput, setTagInput] = useState('');

  const handleAddTag = () => {
    if (tagInput && !tags.includes(tagInput)) {
      setTags([...tags, tagInput]);
      setTagInput('');
    }
  };

  return (
    <div>
      <input
        type="text"
        value={tagInput}
        onChange={(e) => setTagInput(e.target.value)}
        placeholder="Add a tag"
      />
      <button onClick={handleAddTag}>Add Tag</button>
      <div>
        {tags.map((tag, index) => (
          <span key={index}>{tag}</span>
        ))}
      </div>
    </div>
  );
}

export default TagInput;
