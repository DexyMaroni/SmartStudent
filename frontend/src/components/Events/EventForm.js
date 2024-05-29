// frontend/src/components/Events/EventForm.js
import React, { useState } from 'react';

function EventForm({ onCreateEvent }) {
  const [title, setTitle] = useState('');
  const [date, setDate] = useState('');
  const [reminder, setReminder] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const event = { title, date, reminder };
    onCreateEvent(event); // Send this event to the backend or parent component
    setTitle('');
    setDate('');
    setReminder('');
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
        <label>Date:</label>
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
      </div>
      <div>
        <label>Reminder:</label>
        <input
          type="datetime-local"
          value={reminder}
          onChange={(e) => setReminder(e.target.value)}
        />
      </div>
      <button type="submit">Create Event</button>
    </form>
  );
}

export default EventForm;
