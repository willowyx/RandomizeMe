# Randomize Me!

---

### _what is it?_

you input lists, and it makes randomized sentences from them!

(and!!) it uses seed generation so you can return to the same results, or construct them yourself!

also you can add more lists, so that's neat too.

or if you're feeling extra fancy you can also change the sentences if you want 

### _do I need this?_

yes, of course you do.

### _what features can I expect in the future?_

in no particular order, these are some things I'm planning to add soon:
1. mac release. also maybe one for arch btw
2. fusion ui (or at least a dark mode)
3. uwu mode (obviously)
4. maybe a gui list or sentence editor, not sure if that's really feasible tho
5. some sort of better error handler

### _why is it being flagged by my antivirus?_

I went through extra steps to make sure the releases are antivirus-friendly, but windows does rather frequently
flag python executables because they're often used to write malicious content. If you'd rather
check the code and build it yourself, you can use the steps below.

### _how can I build it myself?_
you can use the ```pkg``` directory  to find build files you'll need, and use ```pyinstaller``` or a similar tool to build it.
If you're not sure how to go about it, start with these resources:

- [Install python](https://www.python.org/downloads/)
- [Install pyinstaller](https://www.pyinstaller.org/en/stable/installation.html)
- [Use pyinstaller](https://pyinstaller.org/en/v4.1/usage.html)

Additional notes:
- You'll also need to install the dependencies listed in ```requirements.txt``` in the project's virtual environment.
- An NSIS install script ```randomize_better.nsi``` is included in the ```pkg``` directory if you wish to use the NSIS installer.

---

**made with :3**