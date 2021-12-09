class ThreadsController < ApplicationController
  def show
    @thread = ForumThread.find(params[:id])
    @board = Board.find(@thread.board_id)
    @posts = Post.where(thread_id: @thread.id)
  end

  def new
    # TODO
  end

  def delete
    # TODO
  end
end
