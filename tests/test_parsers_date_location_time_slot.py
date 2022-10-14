import datetime

from bs4 import BeautifulSoup

from signup_genius.parsers.date_location_time_slot import Parser


def test_date_location_time_slot(date_location_time_slot):
    html = open(date_location_time_slot).read()
    html = html.replace(
        '<!--<div><span class="glyphicon glyphicon-ok-sign SUGicon"></span>-->',
        '<div><!--<span class="glyphicon glyphicon-ok-sign sugicon"></span>-->',
    )
    soup = BeautifulSoup(html, "html.parser")
    parser = Parser(soup)
    signups = parser.parse()
    assert len(signups) == 139
    assert sum(s.count for s in signups) == 162
    assert hasattr(signups[0], "slot"), "Signup should have a slot"
    assert signups[0].slot.date == datetime.date(2022, 10, 15)
    assert signups[0].slot.location == "Lake Chabot"
