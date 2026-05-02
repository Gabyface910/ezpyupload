# FAQ
This is the FAQ for ezpyupload.
### Is this a legitimate way to upload a package?
Yes, this is a real way to do it. Check out `nomnomnom`, a useless Python package made to test ezpyupload. Try it with this:
```
pip install nomnomnom
python3 -m nomnomnom
```
`nomnomnom` is the first of many packages to be uploaded by ezpyupload.
### Did PyPI make this or endorse it in any way?
No, PyPI did not endorse ezpyupload. It is an unofficial but functional system to upload stuff to PyPI.
### What OS is supported?
As of April 30, 2026, ezpyupload has been upgraded from YAD (Yet Another Dialog) to more native `tkinter` libraries. This means ezpyupload can be run on __ANY__ OS! (Just make sure your system has graphics 🤓)
ezpyupload has been tested on:
- Debian Linux
- Windows 11
### How do I upload a package?
To upload a package using ezpyupload, run this command.
```bash
export PYTHONIOENCODING=utf-8
# ^
# | Make sure to run this before python3 -m if you're on Linux. Watch the terminal afterwards. If it throws a massive error, turn that on
# If you don't, ezpyupload will return an error
python3 -m ezpyupload
```
Check the box and locate the folder you are uploading from. Select the folder from the dropdown and paste your PyPI API token (available from [pypi.org](https://pypi.org)) into the text box. Click `[Launch]` and you're off!
### How does ezpyupload work?
It's simple:
1. ezpyupload opens `tkinter` and gives you your GUI.
2. `python -m build` and `python -m twine upload dist/*` run in the background. This uploads your package.
3. Best of all, ezpyupload doesn't collect any information about your stuff! Obviously, if it's in PyPI, it's public, but ezpyupload doesn't track stuff.

That's everything!
