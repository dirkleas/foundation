# foundation

foundation set of cli/tui tools for GST!!! of course, this also installs
[claude code](https://claude.com/product/claude-code) and a skill or two...

## setup

start by defining an environment variable in your `.zshrc` startup script
specifying where you work on projects the foundation tools will help you with
-- we call them "h4x" for strategic hacks...

for example, if you want **h4x** in your home diretory, you'd add the following:

```bash
export H4X=$HOME/h4x
```

now complete complete setup as following:

1. install [homebrew](https://brew.sh)
2. install foundation tools

    ```bash
    brew install ghostty espanso stow neovim lazygit lazydocker yazi gdu \
        direnv eza fzf atuin zoxide carapace starship jq yq bat git btop uv \
        --cask claude-code --cask karabiner-elements
    ```

3. install lazyvim distro to supercharge stock neovim

    ```bash
    mv ~/.config/nvim{,.bak} > /dev/null
    git clone https://github.com/LazyVim/starter ~/.config/nvim
    rm -rf ~/.config/nvim/.git
    ```

4. run espanso and karabiner apps, considering default prompts
5. configure foundation tools

    ```bash
    stow --target $HOME stow foundation lazyvim direnv gcam ghostty espanso karabiner
    echo source ~/.foundation >> ~/.zshrc
    espanso service register # considering default prompts
    ```

6. restart ghostty and enjoy!

## roadmap

1. project and time tracking (e.g. [taskwarrior](https://taskwarrior.org/),
[timewarrior](https://timewarrior.net/),
[tock](https://github.com/kriuchkov/tock), and
[flow/kanban](https://github.com/jsubroto/flow))
2. keyboard optimization/mapping (e.g.
[karabiner-elements](https://karabiner-elements.pqrs.org/),
[bettertouchtool](https://folivora.ai/), etc. for `esc`=>`jj`)
3. snippets support (e.g. neovim schema-driven completion vs system-wide
[espanso](https://espanso.org/) with keyboard shortcuts via
[hammerspoon](https://www.hammerspoon.org/))
4. neovim distro (e.g. [lazyvim](https://www.lazyvim.org/))
5. [raycast](https://www.raycast.com/) as spotlight replacement + ai
6. developer tools spectrum and toolchain management (e.g. stow -> nix)
7. dotfile personalization
8. terminal multiplexer (e.g. [tmux](https://github.com/tmux/tmux/wiki) or
[zellij](https://zellij.dev/)) vs tiling manager (e.g.
[aerospace](https://github.com/nikitabobko/AeroSpace))
9. containerization (e.g. [docker](https://www.docker.com/))
10. servers and services -- cloud vs local
