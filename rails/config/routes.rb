Rails.application.routes.draw do
  get 'forum/index'

  resources :boards
  resources :threads
  resources :posts

  root 'forum#index'
end
