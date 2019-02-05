# initial installation instructions

When setting up a new mac:

* install xcode via app store
* install homebrew - see website


```
brew cask install atom \
  firefox \
  google-chrome \
  spectacle \
  virtualbox \
  vagrant
```

* install deps via brew

```
brew install bash \
  byobu \
  git \
  coreutils \
  findutils \
  node \
  python \
  zsh
```

* install virtualenvwrapper

`python -m pip install virtualenvwrapper`

* install oh-my-zsh

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

* `python bootstrap.py`

* pick your theme from https://github.com/robbyrussell/oh-my-zsh/wiki/Themes and add it to your .zshrc.

* `source ~/.osx` to update OSX settings to be more developer friendly
