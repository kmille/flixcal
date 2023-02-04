import json
from pathlib import Path
from flixcal import parse_json


def test_parse_json():
    with open(Path(__file__).parent / Path("backend-response.json")) as f:
        json_data = json.load(f)
    buchungsnummer, cal = parse_json(json_data)
    assert buchungsnummer == "3056658025"
    assert len(cal.events) == 2
