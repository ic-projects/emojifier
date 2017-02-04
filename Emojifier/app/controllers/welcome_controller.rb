class WelcomeController < ApplicationController

  def index

  end

  def pyscript
    pid = fork do
      exec "python lib/assets/py/Main.py 2>&1"
    end
    Process.detach(pid)
  end

  def pysave
    # expects a JSON with @item as name and fields :input of type :string
    input = params[:item][:input]


    #get ML output
    output = 'CAll python script idiot in the pysave controlelr'

    jsonitem = ActionController::Parameters.new({
                                                      item: {
                                                        input: input,
                                                        output: output
                                                  }
                                                  })

    @item =  Item.new(jsonitem.require(:item).permit(:input, :output))

    @item.save

    render :json => jsonitem
  end
end
