lock "~> 3.10.0"

set :application, "pi-printer"
set :repo_url,  "git@github.com:joeyschoblaska/pi-printer"
set :deploy_to, "/home/pi/pi-printer"
set :public_children, []
set :use_sudo, false

task :println do
  line = ARGV.drop(2).join(" ")

  on roles(:app) do
    execute "cd #{current_path} && python python/println.py #{line}"
  end
end
