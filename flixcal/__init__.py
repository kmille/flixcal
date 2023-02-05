import sys
import requests
from urllib.parse import unquote
import arrow
from pathlib import Path

from ics import Calendar, Event
from ics.alarm import DisplayAlarm

import browser_cookie3


def get_json_data():
    domain = "shop.flixbus.de"
    # looks in all browsers for cookies
    cookies = browser_cookie3.load(domain_name=domain)
    if len(cookies) == 0:
        print("Error: Could not find any cookies.")
        sys.exit(1)
    resp = requests.get("https://shop.flixbus.de/booking/success/eventOrder", cookies=cookies)
    # TODO: check for content-type: json
    resp.raise_for_status()
    return resp.json()


def parse_json(j):
    cal = Calendar()
    b = j['id']
    buchungsnummer = f"{b[0:3]} {b[3:6]} {b[6:]}"
    print(f"Buchungsnummer: {buchungsnummer}")
    for _, fahrt in j['items'].items():
        stations = fahrt['stations']
        src = stations['from']['city_name']
        dst = stations['to']['city_name']
        name = f"{src} -> {dst}"
        print(f"Fahrt: {name}")

        depature = arrow.get(stations['from']['departure'])
        arrival = arrow.get(stations['to']['arrival'])
        format = "ddd DD.MM.YY HH:mm"
        fromto = f"{depature.format(format)} -> {arrival.format(format)}"
        print(fromto)

        # expectation: no change to another train
        ticket = fahrt['tickets'][0]
        seat = ticket['premium_seats'][0]['label']
        wagen = ticket['premium_seats'][0]['coach']
        zugnummer = stations['from']['line_direction']['code']
        direction = stations['from']['line_direction']['direction']
        qr_code_data = unquote(fahrt['qr_data'])
        qr = f"https://chart.apis.google.com/chart?cht=qr&chs=300x300&chl={qr_code_data}"
        description = f"Wagen {wagen} Sitz {seat}\nZug: {zugnummer} Richtung {direction}\nQR: {qr}"
        print(description)

        alarm = DisplayAlarm(display_text=name,
                             trigger=depature.shift(hours=-2))
        e = Event()
        e.name = name
        e.begin = depature
        e.end = arrival
        e.description = description
        e.alarms = (alarm, )
        cal.events.add(e)
        print()
    return b, cal


def main():
    json_data = get_json_data()
    buchungsnummer, cal = parse_json(json_data)
    out_file = Path(f"~/Downloads/FLX-{buchungsnummer}.ics")
    with Path(out_file).expanduser().open("w") as f:
        f.write(cal.serialize())
    print(f"ics written to {out_file}")


if __name__ == '__main__':
    main()
