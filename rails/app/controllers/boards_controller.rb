class BoardsController < ApplicationController
  def index
    @boards = Board.all
    @logged_out = false # TODO
  end

  def show
    @board = Board.find(params[:id])
    @threads = ForumThread.where(board_id: @board.id)
  end

  def new
    @board = Board.new(params[:board])
    if @board.save
      redirect_to @board
    else
      render 'new'
    end
  end

  def delete
    render 'boards/index' # TODO
  end
end
