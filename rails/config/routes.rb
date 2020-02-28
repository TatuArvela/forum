Rails.application.routes.draw do
  get '/', to: redirect('/boards')
  get '/boards', to: 'boards#boards'
  get 'boards/0/', to: 'boards#board_topics'
  get 'boards/0/new/', to: 'boards#new_topic'
  get 'topics/0/', to: 'boards#topic_replies'
end
