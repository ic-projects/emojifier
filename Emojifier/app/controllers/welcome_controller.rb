class WelcomeController < ApplicationController
  def index
    @output = %x`python lib/assets/py/py_test.py BITACH`
    render :text => @output
  end
end
