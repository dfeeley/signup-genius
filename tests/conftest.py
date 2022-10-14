import pytest


from signup_genius.parsers.rsvp_adult_child import Signup


@pytest.fixture
def html_path(pytestconfig):
    return pytestconfig.rootpath / "tests" / "html"


@pytest.fixture
def date_time_slot(html_path):
    return html_path / "date-time-slot.htm"


@pytest.fixture
def date_location_time_slot(html_path):
    return html_path / "date-location-time-slot.htm"


@pytest.fixture
def rsvp_adult_child(html_path):
    return html_path / "rsvp-adult-child.htm"


@pytest.fixture
def known_names():
    return [
        "Brad Jones",
        "Conor Watts",
        "Declan Wright",
        "Dave Batty",
        "Jeffrey Adams",
        "Paul T. Malone",
    ]


@pytest.fixture
def signups():
    return [
        Signup(
            name="Bradley Jones",
            response="Yes",
            adult_count=1,
            child_count=0,
            comments="",
        ),
        Signup(
            name="Conor Watts", response="No", adult_count=1, child_count=1, comments=""
        ),
        Signup(
            name="declan wright",
            response="Yes",
            adult_count=0,
            child_count=2,
            comments="",
        ),
        Signup(
            name="david batty",
            response="Yes",
            adult_count=1,
            child_count=0,
            comments="",
        ),
        Signup(
            name="Jeff Adams", response="Yes", adult_count=1, child_count=0, comments=""
        ),
        Signup(
            name="Paul Malone",
            response="Yes",
            adult_count=1,
            child_count=0,
            comments="",
        ),
    ]
