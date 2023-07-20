from flask import render_template, Blueprint, request

from models.event_list import Event
from models.event_list import events

events_blueprint = Blueprint("events", __name__)

# INDEX, display all events
@events_blueprint.route('/events')
def index():
    return render_template("index.jinja", title="Events page", event_list=events)

#CREATE a new event
@events_blueprint.route('/events', methods=["POST"])
def create_event():
    # get fields from the form
    name = request.form["name"]
    date = request.form["date"]
    location = request.form["location"]
    number_of_guests = request.form["num_of_guests"]
    description = request.form["description"]
    # create new event using the fields
    new_event = Event(name, date, number_of_guests, location, description) 
    # add the new event to the list of events
    events.append(new_event)
    #return render_template
    return render_template("index.jinja", title="Events page", event_list=events)