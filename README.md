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

1. clone `foundation` repo into `$H4X` folder

    ```bash
    git clone https://github.com/dirkleas/foundation
    ```

2. install [homebrew](https://brew.sh)
3. install foundation tools

    ```bash
    brew bundle
    ```

4. install lazyvim distro to supercharge stock neovim

    ```bash
    mv ~/.config/nvim{,.bak} > /dev/null
    git clone https://github.com/LazyVim/starter ~/.config/nvim
    rm -rf ~/.config/nvim/.git
    ```

5. run espanso and karabiner apps, considering default prompts
6. configure foundation tools

    ```bash
    stow --target $HOME stow foundation lazyvim direnv gcam ghostty espanso karabiner
    echo source ~/.foundation >> ~/.zshrc
    espanso service register # considering default prompts
    ```

7. restart ghostty and enjoy!

*reminder: periodically run `fupd` to keep foundation tools up-to-date...*

## rationale

why foundation? we want to optimize the things we need to do most often,
reallocate our "thinking" to real tasks, not custodial tasks. here's a summary
of the core foundation tools:

1. [atuin](https://github.com/atuinsh/atuin) - magical shell history with
    SQLite database and encrypted sync
2. [bat](https://github.com/sharkdp/bat) - cat clone with syntax highlighting,
    line numbers, and Git integration
3. [btop](https://github.com/aristocratos/btop) - resource monitor for
    processor, memory, disks, network, and processes
4. [carapace](https://github.com/carapace-sh/carapace-bin) - multi-shell
    completion binary for POSIX and non-POSIX shells
5. [clipboard](https://github.com/Slackadays/Clipboard) - cut, copy, and paste
    anything, anywhere, all from the terminal
6. [claude-code](https://github.com/anthropics/claude-code) - agentic coding
    tool that lives in your terminal and understands your codebase
7. [direnv](https://github.com/direnv/direnv) - loads and unloads environment
    variables based on current directory
8. [espanso](https://github.com/espanso/espanso) - privacy-first,
    cross-platform text expander written in Rust
9. [eza](https://github.com/eza-community/eza) - modern ls replacement with
    colors, symlinks, and Git integration
10. [ffmpeg](https://github.com/FFmpeg/FFmpeg) - complete, cross-platform
    solution to record, convert, and stream audio and video
11. [fzf](https://github.com/junegunn/fzf) - general-purpose command-line
    fuzzy finder
12. [gdu](https://github.com/dundee/gdu) - fast disk usage analyzer with
    console interface written in Go
13. [ghostty](https://github.com/ghostty-org/ghostty) - fast, feature-rich
    terminal emulator with GPU acceleration
14. [git](https://github.com/git/git) - distributed version control system
15. [jq](https://github.com/jqlang/jq) - lightweight command-line JSON
    processor
16. [karabiner-elements](https://github.com/pqrs-org/Karabiner-Elements) -
    powerful keyboard customization tool for macOS
17. [lazydocker](https://github.com/jesseduffield/lazydocker) - simple
    terminal UI for Docker and Docker Compose
18. [lazygit](https://github.com/jesseduffield/lazygit) - simple terminal UI
    for git commands
19. [neovim](https://github.com/neovim/neovim) - Vim-fork focused on
    extensibility and usability
20. [starship](https://github.com/starship/starship) - minimal, blazing-fast,
    customizable prompt for any shell
21. [stow](https://github.com/aspiers/stow) - symlink farm manager for
    dotfiles
22. [uv](https://github.com/astral-sh/uv) - extremely fast Python package and
    project manager written in Rust
23. [yazi](https://github.com/sxyazi/yazi) - blazing fast terminal file
    manager written in Rust
24. [yq](https://github.com/mikefarah/yq) - portable command-line YAML, JSON,
    XML, CSV, and TOML processor
25. [zoxide](https://github.com/ajeetdsouza/zoxide) - smarter cd command that
    remembers frequently visited directories

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
5. [raycast](https://www.raycast.com/) as spotlight replacement, ai,
application shortcuts
6. [superwhisper](https://superwhisper.com/) +
[macrowhisper](https://github.com/ognistik/macrowhisper) for voice user
interface (vui)
7. developer tools spectrum and toolchain management (e.g. stow -> nix)
8. dotfile personalization
9. secure, shared, secrets (e.g. [gopass](https://github.com/gopasspw/gopass)
vs [pass](https://www.passwordstore.org/))
10. terminal multiplexer (e.g. [tmux](https://github.com/tmux/tmux/wiki) or
[zellij](https://zellij.dev/)) vs tiling manager (e.g.
[aerospace](https://github.com/nikitabobko/AeroSpace))
11. containerization (e.g. [docker](https://www.docker.com/))
12. servers and services -- cloud vs local
13. create skill to keep tools docs referenced above up-to-date

## considerations

1. add `.editorconfig` to `.envrc` for repo defaults
