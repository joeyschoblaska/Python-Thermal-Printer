lock "~> 3.10.0"

set :application, "pi-printer"
set :repo_url,  "git@github.com:joeyschoblaska/pi-printer"
set :scm, :git
set :deploy_to, "/home/pi/pi-printer"
set :public_children, []
set :use_sudo, false

# task :invoke do
#   on roles(:app) do
#     execute "cd #{current_path} && bundle exec rake #{ENV["task"] || ENV["TASK"]}"
#   end
# end
