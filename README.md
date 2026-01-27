# foundation

foundation set of cli/tui tools for GST!!! of course, this also installs
[claude code](https://claude.com/product/claude-code) and a skill or two...

## rationale

why foundation? we want to optimize the things we need to do most often,
reallocate our "thinking" to real tasks, not custodial tasks

why add cli/tui in addition to gui apps/tools?

gui apps/tools seem simpler at first glance -- point, click, done. but
that simplicity is a tradeoff:

- **surface consistency, deep chaos**: every app invents its own UX patterns.
  multiply by device, OS, and platform variations. what you learned in one
  context rarely transfers cleanly.
- **hidden state**: where did that setting go? what's actually selected? GUIs
  obscure the state of your system behind layers of menus and modals.
- **geometry struggles**: resolution, scaling, window layouts -- an endless
  negotiation between what you want and what the app allows.
- **automation gap**: scripting GUIs is fragile at best. even state-of-the-art
  AI models struggle to reliably orchestrate graphical interfaces.

cli/tui tools take a different path:

- **explicit**: commands say exactly what they do. no hunting through menus.
- **repeatable**: same input, same output. every time.
- **composable**: small tools that do one thing well, piped together.
- **automatable**: scripts, aliases, hooks -- your workflow becomes code.
- **version-controllable**: text configs live in git. diff, blame, revert.
- **ai-native**: LLMs reason about text naturally. your tools become
  orchestratable.

this isn't about abandoning GUIs entirely. browsers, media editors, visual
design tools -- some work genuinely requires graphical feedback. foundation
provides the cli/tui layer for everything else: the daily operations where
clarity, repeatability, and automation matter most.

## setup

start by defining an environment variable in your `.zshrc` startup script
specifying where you work on projects the foundation tools will help you with
-- we call them "h4x" for strategic hacks...

for example, if you want **h4x** in your home diretory, you'd add the following:

```bash
export H4X=$HOME/h4x
```

now complete complete setup as following:

1. clone `foundation` repo into `$H4X` folder:

    ```bash
    git clone https://github.com/dirkleas/foundation
    ```

2. install [homebrew](https://brew.sh)
3. install foundation tools:

    ```bash
    brew bundle
    ```

4. install [claude-code](https://code.claude.com/docs/en/setup)
5. install lazyvim distro to supercharge stock neovim:

    ```bash
    mv ~/.config/nvim{,.bak} > /dev/null
    git clone https://github.com/LazyVim/starter ~/.config/nvim
    rm -rf ~/.config/nvim/.git
    ```

6. run `espanso` and `karabiner` apps, considering default prompts
7. configure foundation tools:

    ```bash
    stow --target $HOME stow foundation lazyvim direnv gcam ghostty espanso karabiner
    echo source ~/.foundation >> ~/.zshrc
    espanso service register # considering default prompts
    ```

8. restart `ghostty` and enjoy!

*reminder: periodically run `fupd` to keep foundation tools up-to-date...*

## tools

here's a summary of the core cli/tui/gui foundation tools:

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
6. [direnv](https://github.com/direnv/direnv) - loads and unloads environment
    variables based on current directory
7. [dvc](https://github.com/iterative/dvc) - version control for large files
    like media and datasets with cloud storage backends
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
13. [gh](https://github.com/cli/cli) - GitHub's official command line tool
14. [ghostty](https://github.com/ghostty-org/ghostty) - fast, feature-rich
    terminal emulator with GPU acceleration
15. [git](https://github.com/git/git) - distributed version control system
16. [git-lfs](https://github.com/git-lfs/git-lfs) - Git extension for
    versioning large files
17. [jj](https://github.com/jj-vcs/jj) - Git-compatible VCS that is both
    simple and powerful
18. [jq](https://github.com/jqlang/jq) - lightweight command-line JSON
    processor
19. [karabiner-elements](https://github.com/pqrs-org/Karabiner-Elements) -
    powerful keyboard customization tool for macOS
20. [lazydocker](https://github.com/jesseduffield/lazydocker) - simple
    terminal UI for Docker and Docker Compose
21. [lazygit](https://github.com/jesseduffield/lazygit) - simple terminal UI
    for git commands
22. [neovim](https://github.com/neovim/neovim) - Vim-fork focused on
    extensibility and usability
23. [starship](https://github.com/starship/starship) - minimal, blazing-fast,
    customizable prompt for any shell
24. [stow](https://github.com/aspiers/stow) - symlink farm manager for
    dotfiles
25. [uv](https://github.com/astral-sh/uv) - extremely fast Python package and
    project manager written in Rust
26. [yazi](https://github.com/sxyazi/yazi) - blazing fast terminal file
    manager written in Rust
27. [yq](https://github.com/mikefarah/yq) - portable command-line YAML, JSON,
    XML, CSV, and TOML processor
28. [zoxide](https://github.com/ajeetdsouza/zoxide) - smarter cd command that
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
11. configuration management (e.g. [git](https://git-scm.com/),
[jujitsu](https://github.com/jj-vcs/jj),
[dvc](https://dvc.org/), [gerrit](https://www.gerritcodereview.com/),
[gitea](https://github.com/go-gitea/gitea),
[forgejo](https://codeberg.org/forgejo/forgejo), etc.)
12. containerization (e.g. [docker](https://www.docker.com/),
[portainer](https://www.portainer.io/),
[lima](https://github.com/lima-vm/lima),
[colima](https://github.com/abiosoft/colima), macos native containers, etc.)
13. servers and services -- cloud vs local
14. leverage ai/frontier model scaffolding mechanisms (e.g. reusable prompts
via tasks, skills, agents, hooks, etc.) to optimize/automate structured
and unstructured worklows

## considerations

1. add `.editorconfig` to `.envrc` for repo defaults
2. longterm use of github given new home in ms ai division
