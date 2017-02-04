class ItemsController < ApplicationController

  def index
    @items = Item.all
  end

  def create
    @item =  Item.new(params.require(:@item).permit(:input, :string, :output, :string))

    @item.save

    redirect_to @item
  end

  def show
    @item = Item.find(params.require(:id))
  end

  def new
  end

end
