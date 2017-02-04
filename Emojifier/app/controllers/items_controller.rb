class ItemsController < ApplicationController

  def index
    @items = Item.all
  end

  def create
    @item =  Item.new(params.require(:@item).permit(:input, :output))

    @item.save

    redirect_to @item
  end

  def show
    @item = Item.find(params.require(:id))
  end

  def new
  end

end
