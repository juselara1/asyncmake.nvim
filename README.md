# asyncmake.nvim
---

<a href="https://pypi.python.org/pypi/asyncmake"><img src="https://img.shields.io/pypi/v/asyncmake.svg"/></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"/></a>

![demo](docs/file.gif)

`asyncmake.nvim` is a Neovim plugin that orchestrates `make` calls asynchronously.

## Installation
---

To install `asyncmake.nvim`, you need to install the Python package via `pip`:

```sh
pip install asyncmake
```

After that, you can use any plugin manager. For example, with `packer`:

```lua
use {
    "juselara1/asyncmake.nvim",
    requires = {
        {"rcarriga/nvim-notify"},
        {"nvim-telescope/telescope.nvim", tag = "0.1.1"},
        {"nvim-lua/plenary.nvim"}
    },
    run = ":UpdateRemotePlugins"
}
```

Add the following line to your `init.lua` file:

```lua
require("asyncmake")
```

## Usage
---

You can use the following commands:

- `:Make [rules]`: launches a `make` command. You can optionally specify some rules. For example, `:Make init test` is equivalent to the terminal command `make init test`.
- `:MakeFuzzy`: launches a Telescope window with the parsed rules. You can trigger a rule from there.

`asyncmake.nvim` automatically finds the root directory of the `Makefile`, so you don't need to be in the same directory as the `Makefile` to execute the commands.
