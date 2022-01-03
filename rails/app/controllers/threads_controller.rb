class ThreadsController < ApplicationController
  def show
    @thread = ForumThread.find(params[:id])
    @board = Board.find(@thread.board_id)
    @posts = Post.where(thread_id: @thread.id)
  end

  def new
    @thread = Thread.new(params[:thread])
    if @thread.save
      redirect_to @thread
    else
      render 'new'
    end
  end

  def delete
    # TODO
  end
end
