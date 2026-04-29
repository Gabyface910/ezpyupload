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
Currently, ezpyupload runs on YAD (Yet Another Dialog), and is only available on Linux. Even if you managed to get YAD, it would be hard to run. The good news is that Linux is __completely free__ and anyone can use it!
ezpyupload has been tested on:
- Debian Linux

That's all!
### How do I upload a package?
To upload a package using ezpyupload, run this command.
```bash
export PYTHONIOENCODING=utf-8
# ^
# | Make sure to run this before python3 -m
# If you don't, ezpyupload will return an error
python3 -m ezpyupload
```
Check the box and locate the folder you are uploading from. Select the folder from the dropdown and paste your PyPI API token (available from [pypi.org](https://pypi.org)) into the text box. Click `[Launch]` and you're off!
### How does ezpyupload work?
It's simple:
1. ezpyupload opens YAD (Yet Another Dialog) and gives you your GUI choices.
2. `python -m build` and `python -m twine upload dist/*` run in the background. This uploads your package.

That's everything!
