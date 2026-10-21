<p align="center">
  <img src="images/logo-512.png" alt="VSx Glow logo" width="160" />
</p>

<h1 align="center">VSx Glow</h1>

<p align="center">
  A Neovim-inspired dark theme for VS Code, blending <b>One Dark Pro</b> and <b>Dracula Official</b>.<br/>
  <b>Developed by SGDEV</b>
</p>

---

## Availability

VSx Glow is available on:

- **Open VSX Registry** — https://open-vsx.org/extension/sgdev/vsx-glow
- **Visual Studio Code Marketplace** — https://marketplace.visualstudio.com/items?itemName=sgdev.vsx-glow

## Features

- **Yellow main text** (`#f1fa8c`) on a deep `#1e222a` One Dark Pro background, with Dracula pink keywords, purple constants, and orange parameters.
- Neovim-style flat UI: darker sidebar, tabs and status bar, bufferline-style tab accent, lualine-style status pill, and floating-window style popups.
- Full workbench, syntax (TextMate), and semantic token support.

## Install

**From a marketplace:** search for **VSx Glow** in the Extensions view (VS Code Marketplace) or in your VSCodium / Open VSX-based editor.

**From the `.vsix` file:**

```bash
code --install-extension vsx-glow-0.1.1.vsix
```

Then press `Ctrl/Cmd+K Ctrl/Cmd+T` and choose **VSx Glow**.

**From source:** copy this folder into `~/.vscode/extensions/vsx-glow` (Windows: `%USERPROFILE%\.vscode\extensions\vsx-glow`) and restart VS Code.

## Make it feel like Neovim

```json
{
  "editor.cursorStyle": "block",
  "editor.cursorBlinking": "solid",
  "editor.lineNumbers": "relative",
  "editor.renderLineHighlight": "all",
  "editor.fontFamily": "'JetBrainsMono Nerd Font', 'FiraCode Nerd Font', monospace",
  "editor.fontLigatures": true,
  "editor.minimap.enabled": false,
  "editor.bracketPairColorization.enabled": true
}
```

For modal editing, install the **VSCode Neovim** extension.

## Palette

| Role | Color |
|---|---|
| Main text | `#f1fa8c` |
| Background | `#1e222a` |
| Sidebar / tabs | `#1a1d23` |
| Floating widgets | `#181b21` |
| Keywords | `#ff79c6` |
| Functions | `#61afef` |
| Strings | `#98c379` |
| Numbers / constants | `#bd93f9` |
| Types / classes | `#8be9fd` |
| Properties / tags | `#e06c75` |
| Parameters | `#ffb86c` |
| Operators | `#56b6c2` |
| Comments | `#6b7694` |

## Build from source

```bash
npm i -g @vscode/vsce
vsce package        # creates vsx-glow-0.1.1.vsix
```

Regenerate the logo with `python3 make_logo.py` (requires Pillow).

## Links & contact

- **Website:** https://vsx-glow.sgdev.qd.je
- **Developer:** SGDEV
- **Email:** info@sgdev.qd.je

## License

Copyright (C) 2026 SGDEV.

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file or <https://www.gnu.org/licenses/gpl-3.0.html>.

One Dark Pro and Dracula Official are separate projects by their respective authors; VSx Glow is an independent theme inspired by their color styles. The logo is an original stylized mark and is not affiliated with or endorsed by Microsoft.
