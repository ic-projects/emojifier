class WelcomeController < ApplicationController

  def index

  end

  def pyscript
    pid = fork do
      exec "python lib/assets/py/Main.py 2>&1"
    end
    Process.detach(pid)
  end
end
