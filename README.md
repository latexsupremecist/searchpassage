## searchpassage

Search for bible passages from the terminal.

#### Usage

1. Run `main.py`
2. You will be prompted to enter a version and bible passage. The format should be `[version] [book] [passage]`, where passages should be in the form `a:b`, `a:b-c`, `a:b-c:d`, or `a`. Note that all input is case insensitive.

	E.g. `kjv psalms 23:1-6`

You can add your own `.json` versions, or edit `dict.py` to include your preferred abbreviations.
