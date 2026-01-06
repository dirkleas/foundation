# foundation

base set of cli/tui tools for GST!!! of course, this also installs 
[claude code](https://claude.com/product/claude-code) and a skill or two...

## setup

start by defining an environment variable in your `.zshrc` startup script specifying
where you work on projects the foundation tools will help you with -- we call them "h4x"
for strategic hacks...

for example, if you want **h4x** in your home diretory, you'd add the following:


```
export H4X=$HOME/h4x
```

now complete complete setup as following:

1. install [homebrew](https://brew.sh/)
2. `brew install ghostty espanso stow neovim lazygit lazydocker yazi gdu direnv eza fzf atuin zoxide carapace starship` 
3. `brew install --cask claude-code`
4. `stow --target $HOME stow foundation gcam ghostty espanso`
5. `echo source ~/.foundation >> ~/.zshrc`
6. `espanso service register` # accept defaults
7. `source ~/.zshrc`
8. enjoy!

## update

1. `stow foundation`
2. enjoy!

no need to repeat sourcing foundation tools from `./zshrc`

## roadmap

1. snippents support (e.g. neovim schema-driven json completion vs system-wide [espanso](https://espanso.org/), [textpander $$](http://textexpander.com/)) triggered via via keyboard shortcuts using [hammerspoon](https://www.hammerspoon.org/)(https://www.hammerspoon.org/)
2. neovim distro (e.g. [astronvim](https://astronvim.com/) or [lazyvim](https://www.lazyvim.org/))
3. developer tools
4. dotfile personalization
5. terminal multiplexer (e.g. [tmux](https://github.com/tmux/tmux/wiki) or [zellij](https://zellij.dev/))
6. containerization (e.g. [docker](https://www.docker.com/))
7. servers and services -- cloud vs local

