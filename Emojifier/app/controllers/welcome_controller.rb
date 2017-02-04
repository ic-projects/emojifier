class WelcomeController < ApplicationController

  def index
    @items = Item.all
  end

  def pyscript
    # expects a JSON with @item as name and fields :input of type :string
    input = params[:item][:input]


    #get ML output
    thr = Thread.new { puts "Whats the big deal" }


    output = ''



    jsonitem = ActionController::Parameters.new({
                                                    item: {
                                                        input: input,
                                                        output: output
                                                    }
                                                })
    render :json => jsonitem
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
