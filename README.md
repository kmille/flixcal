# flixtrain ics generator

Flixtrain does not give you a .ics file to import. This code generates a ics file with all rides of your order. In order to do so, it uses chromiums cookies and sends a request to flixtrain's backend (https://shop.flixbus.de/booking/success/eventOrder). It's best if your are done with the order and see the summary of your order to run the script (you will see https://shop.flixbus.de/booking/success in your browser). After parsing the json, it generats an ics and saves it into your Downloads directory.

# How to use it

```bash
git clone https://github.com/kmille/flixcal.git
cd flixcal
poetry install
poetry run pytest -v -s
poetry build
python -m venv venv
source venv/bin/activate
pip install dist/flixcal-0.1.0-py3-none-any.whl
flixcal-generator

You can also use `pip install --user dist/flixcal-0.1.0-py3-none-any.whl`
```

If you are on Arch Linux, you can use the PKGBUILD in the arch directory. But you need to run `pip install --user pycookiecheat` as there is no AUR package for.

# Running the tests
```bash
kmille@linbox:flixcal poetry run pytest -v -s
============================================================================================================= test session starts =============================================================================================================
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0 -- /home/kmille/.cache/pypoetry/virtualenvs/flixcal-CBUX2rok-py3.10/bin/python
cachedir: .pytest_cache
rootdir: /home/kmille/projects/flixcal
collected 1 item                                                                                                                                                                                                                              

tests/test_flixcal.py::test_parse_json Buchungsnummer: 305 665 8025
Fahrt: Darmstadt -> Freiburg (i.Br.)
Thu 23.03.23 15:57 -> Thu 23.03.23 18:33
Wagen 3 Sitz 24D
Zug: FLX10 Richtung Basel Bad Bf
QR: https://chart.apis.google.com/chart?cht=qr&chs=300x300&chl=https://shop.flixbus.de/pdfqr/3056658025/9vxr2qtujjoynqxct2pcck4q19hi0piy5fmai9p9zxyh9hmd0a?trip=direct:183882293:20648:26168

Fahrt: Freiburg (i.Br.) -> Darmstadt
Mon 27.03.23 09:59 -> Mon 27.03.23 12:48
Wagen 3 Sitz 3A
Zug: FLX10 Richtung Berlin Hbf
QR: https://chart.apis.google.com/chart?cht=qr&chs=300x300&chl=https://shop.flixbus.de/pdfqr/3056658025/9vxr2qtujjoynqxct2pcck4q19hi0piy5fmai9p9zxyh9hmd0a?trip=direct:183879973:26168:20648

PASSED

============================================================================================================== 1 passed in 0.15s ==========================================================================================
```
