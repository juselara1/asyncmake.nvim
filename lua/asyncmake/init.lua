local function make_command(args)
    vim.cmd("MakeFn")
end
vim.api.nvim_create_user_command("Make", make_command)
