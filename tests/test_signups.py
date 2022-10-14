import datetime

import pytest

from signup_genius import get_signups, get_signups_from_html


def test_signups_from_html(date_time_slot):
    signups = get_signups_from_html(date_time_slot.read_text())
    assert len(signups) == 151
    assert sum(s.count for s in signups) == 191
    assert signups[0].name == "Betty Bethune"
    assert hasattr(signups[0], "slot"), "Signup should have a slot"
    assert signups[0].slot.date == datetime.date(2022, 10, 5)


@pytest.mark.internet
def test_signups_from_url():
    url = "https://www.signupgenius.com/go/10c0c4aa8a82cabfdc61-sierra"
    signups = get_signups(url, refresh=False)
    assert len(signups) > 0
    assert signups[0].name == "Jake Mikalis"
    first = signups[0]
    assert first.response == "Yes"


def test_signups_from_html_with_name_mapping(date_time_slot):
    name_mapping = {"John Hertel": "John B. Hertel"}
    signups = get_signups_from_html(
        date_time_slot.read_text(), name_mapping=name_mapping
    )
    names = {s.name for s in signups}
    assert "John B. Hertel" in names
    assert "John Hertel" not in names


def test_signups_from_html_with_fuzzy_match(date_time_slot):
    match_names = ["John B. Hertel", "Another Person"]
    signups = get_signups_from_html(date_time_slot.read_text(), match_names=match_names)
    names = {s.name for s in signups}
    assert "John B. Hertel" in names
    assert "John Hertel" not in names
