from flask import Blueprint, request, jsonify
from app import db
from datetime import datetime
from app.events.models import Event
from flask_login import login_required, current_user

events_bp = Blueprint('events', __name__)

@events_bp.route('/events', methods=['POST'])
@login_required
def create_event():
    data = request.get_json()
    new_event = Event(
        title=data['title'],
        description=data.get('description'),
        date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
        time=datetime.strptime(data['time'], '%H:%M').time(),
        reminder=data.get('reminder', False),  # Reminder field
        user_id=current_user.id
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event created successfully!'}), 201


@events_bp.route('/events', methods=['GET'])
@login_required
def get_events():
    events = Event.query.filter_by(user_id=current_user.id).all()
    return jsonify([event.serialize() for event in events]), 200

@events_bp.route('/events/<int:event_id>', methods=['PUT'])
@login_required
def update_event(event_id):
    data = request.get_json()
    event = Event.query.get(event_id)
    if event and event.user_id == current_user.id:
        event.title = data['title']
        event.description = data.get('description')
        event.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        event.time = datetime.strptime(data['time'], '%H:%M').time()
        event.reminder = data.get('reminder', False)
        db.session.commit()
        return jsonify({'message': 'Event updated successfully!'}), 200
    return jsonify({'message': 'Event not found or unauthorized'}), 404

@events_bp.route('/events/<int:event_id>', methods=['DELETE'])
@login_required
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event and event.user_id == current_user.id:
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted successfully!'}), 200
    return jsonify({'message': 'Event not found or unauthorized'}), 404
