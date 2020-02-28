class BoardsController < ApplicationController
  def boards
    render "boards/index", layout: "boards"
  end

  def board_topics
    render plain: 'topics'
  end

  def new_topic
    render plain: 'new_topic'
  end

  def topic_replies
    render plain: 'topic_replies'
  end
end
