# foundation

foundation set of cli/tui tools for GST!!! of course, this also installs 
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

1. install [homebrew](https://brew.sh)
2. `brew install ghostty espanso stow neovim lazygit lazydocker yazi gdu direnv eza fzf atuin zoxide carapace starship jq yq bat` 
3. `brew install --cask claude-code`
3. `brew install --cask karabiner-elements`
1. run espanso and karabiner apps, considering default prompts
1. run karbiner, considering default prompts
4. `stow --target $HOME stow foundation gcam ghostty espanso karabiner`
5. `echo source ~/.foundation >> ~/.zshrc`
6. `espanso service register` # accept defaults
7. `source ~/.zshrc`
8. enjoy!

## update

1. `stow foundation`
2. enjoy!

no need to repeat sourcing foundation tools from `./zshrc`

## roadmap

1. project and time tracking (e.g. [taskwarrior](https://taskwarrior.org/), [timewarrior](https://timewarrior.net/), and [flow/kanban](https://github.com/jsubroto/flow))
2. keyboard optimization/mapping (e.g. [karabiner-elements](https://karabiner-elements.pqrs.org/), [bettertouchtool](https://folivora.ai/), etc. for `esc`=>`jj`)
3. snippets support (e.g. neovim schema-driven completion vs system-wide [espanso](https://espanso.org/) with keyboard shortcuts via [hammerspoon](https://www.hammerspoon.org/))
4. neovim distro (e.g. [lazyvim](https://www.lazyvim.org/))
1. [raycast](https://www.raycast.com/) as spotlight replacement + ai
5. developer tools spectrum and toolchain management (e.g. stow -> nix)
6. dotfile personalization
7. terminal multiplexer (e.g. [tmux](https://github.com/tmux/tmux/wiki) or [zellij](https://zellij.dev/))
8. containerization (e.g. [docker](https://www.docker.com/))
9. servers and services -- cloud vs local

