local notify = require("notify")
local pickers = require "telescope.pickers"
local finders = require "telescope.finders"
local conf = require("telescope.config").values
local actions = require "telescope.actions"
local action_state = require "telescope.actions.state"

local function make_command(opts)
    local function remote_call()
        cmd = {"MakeFn", opts.args}
        cmd = table.concat(cmd, " ")
        notify("Start: "..cmd)
        vim.api.nvim_exec2(cmd, {})
        notify("End: "..cmd)
    end

    async.run(remote_call)
end

local function make_start_msg(opts)
    cmd = {"make", opts.args}
    cmd = table.concat(cmd, " ")
    notify("Start: "..cmd)
end

local function make_end_msg(opts)
    cmd = {"make", opts.args}
    cmd = table.concat(cmd, " ")
    notify("End: "..cmd)
end

local function make_err(opts)
    cmd = {"make", opts.args}
    cmd = table.concat(cmd, " ")
    notify("Error: "..cmd, "error")
end

vim.api.nvim_create_user_command("MakeStartMsg", make_start_msg, {nargs='?'})
vim.api.nvim_create_user_command("MakeEndMsg", make_end_msg, {nargs='?'})
vim.api.nvim_create_user_command("MakeErr", make_err, {nargs='?'})

local function split(text, sep)
    local t={}
    for str in string.gmatch(text, "([^"..sep.."]+)") do
        table.insert(t, str)
    end
    return t
end

local make_fuzzy = function(opts)
    values = vim.api.nvim_exec2("MakeParsedOpts", {output=true})
    pickers.new(opts, {
        prompt_title = "make",
        finder = finders.new_table {
            results = split(values.output, " ")
        },
        sorter = conf.generic_sorter({}),
        attach_mappings = function(prompt_bufnr, map)
            actions.select_default:replace(function()
                actions.close(prompt_bufnr)
                local selection = action_state.get_selected_entry()
                vim.api.nvim_exec2("Make "..selection[1], {})
            end)
            return true
        end,
    }):find()
end

vim.api.nvim_create_user_command("MakeFuzzy", make_fuzzy, {nargs='?'})
