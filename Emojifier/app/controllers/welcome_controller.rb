class WelcomeController < ApplicationController
  def index
    @output = %x`python lib/assets/py/py_test.py Comand line`
    render :text => @output
  end
end
