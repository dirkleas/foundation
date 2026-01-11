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
    brew install atuin bat btop carapace direnv espanso eza fzf gdu ghostty \
        git jq lazydocker lazygit neovim starship stow uv yazi yq zoxide \
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

*reminder: periodically run `fupd` to keep foundation tools up-to-date...*

## rationale

why foundation? we want to optimize the things we need to do most often,
reallocate our "thinking" to real tasks, not custodial tasks. here's a summary
of the core foundation tools:

1. [atuin](https://github.com/atuinsh/atuin) - magical shell history with SQLite database and encrypted sync
2. [bat](https://github.com/sharkdp/bat) - cat clone with syntax highlighting, line numbers, and Git integration
3. [btop](https://github.com/aristocratos/btop) - resource monitor for processor, memory, disks, network, and processes
4. [carapace](https://github.com/carapace-sh/carapace-bin) - multi-shell completion binary for POSIX and non-POSIX shells
5. [claude-code](https://github.com/anthropics/claude-code) - agentic coding tool that lives in your terminal and understands your codebase
6. [direnv](https://github.com/direnv/direnv) - loads and unloads environment variables based on current directory
7. [espanso](https://github.com/espanso/espanso) - privacy-first, cross-platform text expander written in Rust
8. [eza](https://github.com/eza-community/eza) - modern ls replacement with colors, symlinks, and Git integration
9. [fzf](https://github.com/junegunn/fzf) - general-purpose command-line fuzzy finder
10. [gdu](https://github.com/dundee/gdu) - fast disk usage analyzer with console interface written in Go
11. [ghostty](https://github.com/ghostty-org/ghostty) - fast, feature-rich terminal emulator with GPU acceleration
12. [git](https://github.com/git/git) - distributed version control system
13. [jq](https://github.com/jqlang/jq) - lightweight command-line JSON processor
14. [karabiner-elements](https://github.com/pqrs-org/Karabiner-Elements) - powerful keyboard customization tool for macOS
15. [lazydocker](https://github.com/jesseduffield/lazydocker) - simple terminal UI for Docker and Docker Compose
16. [lazygit](https://github.com/jesseduffield/lazygit) - simple terminal UI for git commands
17. [neovim](https://github.com/neovim/neovim) - Vim-fork focused on extensibility and usability
18. [starship](https://github.com/starship/starship) - minimal, blazing-fast, customizable prompt for any shell
19. [stow](https://github.com/aspiers/stow) - symlink farm manager for dotfiles
20. [uv](https://github.com/astral-sh/uv) - extremely fast Python package and project manager written in Rust
21. [yazi](https://github.com/sxyazi/yazi) - blazing fast terminal file manager written in Rust
22. [yq](https://github.com/mikefarah/yq) - portable command-line YAML, JSON, XML, CSV, and TOML processor
23. [zoxide](https://github.com/ajeetdsouza/zoxide) - smarter cd command that remembers frequently visited directories

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
11. create skill to keep tools docs referenced above up-to-date
