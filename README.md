# foundation

base set of cli/tui tools for GST!!! of course, this also installs 
[claude code](https://claude.com/product/claude-code) and a skill or two...

## setup

complete following:

1. install [homebrew](https://brew.sh/)
2. `brew install stow neovim lazygit lazydocker yazi gdu direnv eza fzf zoxide carapace starship` 
3. `brew install --cask claude-code`
4. `stow --target $HOME foundation gcam`
5. `echo source ~/.foundation >> ~/.zshrc`
6. `source ~/.zshrc`
7. enjoy!

## update

1. `stow foundation`
2. enjoy!

no need to repeat sourcing foundation tools from `./zshrc`

## roadmap

1. neovim distro (e.g. [astronvim](https://astronvim.com/) or [lazyvim](https://www.lazyvim.org/))
2. developer tools
3. dotfile customization
4. terminal multiplexer (e.g. [tmux](https://github.com/tmux/tmux/wiki) or [zellij](https://zellij.dev/))
5. containerization (e.g. [docker](https://www.docker.com/))
6. servers and services -- cloud vs local

