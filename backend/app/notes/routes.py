import logging
from flask import Blueprint, request, jsonify
from app import db
from app.notes.models import Note
from app.auth.models import User
from flask_login import login_required, current_user

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes/create', methods=['POST'])
@login_required
def create_note():
    """
    Create a new note for the authenticated user.

    This function is a route handler for the '/notes/create' endpoint. It expects a POST request with JSON data containing the 'title' and 'content' of the note. The function creates a new Note object with the provided data, sets the 'user_id' to the id of the authenticated user, and adds the note to the database. Finally, it returns a JSON response with a success message and a status code of 201.

    Parameters:
    None

    Returns:
    A JSON response with a success message and a status code of 201.
    """
    data = request.get_json()
    new_note = Note(
        title=data['title'],
        content=data['content'],
        user_id=current_user.id
    )
    db.session.add(new_note)
    db.session.commit()
    return jsonify({'message': 'Note created successfully!'}), 201

@notes_bp.route('/notes', methods=['GET'])
@login_required
def get_notes():
    """
    Retrieves all notes belonging to the authenticated user.

    This function is a route handler for the '/notes' endpoint with the HTTP method 'GET'. It requires the user to be authenticated.

    Returns:
        A JSON response containing a list of serialized note objects belonging to the authenticated user. Each note object has the following attributes:
            - id (int): The unique identifier of the note.
            - title (str): The title of the note.
            - content (str): The content of the note.
            - tags (list): A list of tags associated with the note.
            - created_at (str): The timestamp when the note was created.
            - updated_at (str): The timestamp when the note was last updated.
            - user_id (int): The unique identifier of the user who created the note.

        The HTTP status code of the response is 200.

    Raises:
        None
    """
    logging.info('Fetching notes for user: %s', current_user.id)
    notes = Note.query.filter_by(user_id=current_user.id).all()
    logging.info('Fetched notes: %s', notes)
    return jsonify([note.serialize() for note in notes]), 200

@notes_bp.route('/notes/search', methods=['GET'])
@login_required
def search_notes():
    """
    Search for notes belonging to the authenticated user based on a query.

    This function is a route handler for the '/notes/search' endpoint with the HTTP method 'GET'. It requires the user to be authenticated.

    Parameters:
        None

    Returns:
        A JSON response containing a list of serialized note objects belonging to the authenticated user that match the query. Each note object has the following attributes:
            - id (int): The unique identifier of the note.
            - title (str): The title of the note.
            - content (str): The content of the note.
            - tags (list): A list of tags associated with the note.
            - created_at (str): The timestamp when the note was created.
            - updated_at (str): The timestamp when the note was last updated.
            - user_id (int): The unique identifier of the user who created the note.

        The HTTP status code of the response is 200.

    Raises:
        None
    """
    """
    Search for notes belonging to the authenticated user based on a query.

    This function is a route handler for the '/notes/search' endpoint with the HTTP method 'GET'. It requires the user to be authenticated.

    Parameters:
        None

    Returns:
        A JSON response containing a list of serialized note objects belonging to the authenticated user that match the query. Each note object has the following attributes:
            - id (int): The unique identifier of the note.
            - title (str): The title of the note.
            - content (str): The content of the note.
            - tags (list): A list of tags associated with the note.
            - created_at (str): The timestamp when the note was created.
            - updated_at (str): The timestamp when the note was last updated.
            - user_id (int): The unique identifier of the user who created the note.

        The HTTP status code of the response is 200.

    Raises:
        None
    """
    query = request.args.get('query')
    logging.info('Searching notes for user: %s with query: %s', current_user.id, query)
    notes = Note.query.filter(Note.user_id == current_user.id, 
                              (Note.title.contains(query) | 
                               Note.content.contains(query))).all()
    logging.info('Search results: %s', notes)
    return jsonify([note.serialize() for note in notes]), 200


@notes_bp.route('/notes/share', methods=['POST'])
@login_required
def share_note():
    data = request.get_json()
    note = Note.query.get(data['note_id'])
    if note and note.user_id == current_user.id:
        shared_user = User.query.filter_by(email=data['email']).first()
        if shared_user:
            shared_note = Note(
                title=note.title,
                content=note.content,
                user_id=shared_user.id,
                tags=note.tags
            )
            db.session.add(shared_note)
            db.session.commit()
            return jsonify({'message': 'Note shared successfully!'}), 200
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'Note not found or unauthorized'}), 404

@notes_bp.route('/notes/tag', methods=['POST'])
@login_required
def tag_note():
    """
    Updates the tags of a note for the authenticated user.

    This function is a route handler for the '/notes/tag' endpoint with the HTTP method 'POST'. It requires the user to be authenticated.

    Parameters:
        None

    Returns:
        If the note is found and belongs to the authenticated user, the function updates the tags of the note with the provided data and returns a JSON response with a success message and a status code of 200.
        If the note is not found or does not belong to the authenticated user, the function returns a JSON response with an error message and a status code of 404.

    Raises:
        None
    """
    """
    Updates the tags of a note for the authenticated user.

    This function is a route handler for the '/notes/tag' endpoint with the HTTP method 'POST'. It requires the user to be authenticated.

    Parameters:
        None

    Returns:
        If the note is found and belongs to the authenticated user, the function updates the tags of the note with the provided data and returns a JSON response with a success message and a status code of 200.
        If the note is not found or does not belong to the authenticated user, the function returns a JSON response with an error message and a status code of 404.

    Raises:
        None
    """
    data = request.get_json()
    note = Note.query.get(data['note_id'])
    if note and note.user_id == current_user.id:
        note.tags = data['tags']
        db.session.commit()
        return jsonify({'message': 'Tags updated successfully!'}), 200
    return jsonify({'message': 'Note not found or unauthorized'}), 404

