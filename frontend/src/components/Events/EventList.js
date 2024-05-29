// frontend/src/components/Events/EventList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function EventList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/events')
      .then(response => {
        setEvents(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the events!', error);
      });
  }, []);

  return (
    <div>
      <h2>Events</h2>
      <ul>
        {events.map(event => (
          <li key={event.id}>{event.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default EventList;
